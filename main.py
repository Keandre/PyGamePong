from pygame.locals import *
import pygame
import sys
import time
import sound
from paddle import paddle
from ball import ball
import gui
pygame.init()

WINDOWWIDTH, WINDOWHEIGHT = 600, 600
WINDOW_DIMENSIONS = (WINDOWWIDTH, WINDOWHEIGHT)
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_DIMENSIONS, 0, 32)
PADDLE_VELOCITY = 7

font = pygame.font.Font('fonts/Georgia.ttf', 20)
pong_font = pygame.font.Font('fonts/bit5x3.ttf', 30)
pong_font_title = pygame.font.Font('fonts/bit5x3.ttf', 70)


def main_menu():
    while True:
        DISPLAYSURF.fill(pygame.Color('black'))

        gui.draw_text_center('PONG', pong_font_title,
                             pygame.Color('white'), DISPLAYSURF, 0, 50)
        play_button = gui.button('PLAY', pong_font, pygame.Color(
            'white'),  pygame.Color('yellow'), 0, 150)
        exit_button = gui.button('EXIT', pong_font, pygame.Color(
            'white'), pygame.Color('yellow'), 0, 210)

        mx, my = pygame.mouse.get_pos()

        if play_button.get_rect_centered(DISPLAYSURF).collidepoint(mx, my):
            if click:
                pygame.mixer.Sound.play(sound.menu_click)
                game()
            play_button.draw_text_centered(DISPLAYSURF, hover=True)
        else:
            play_button.draw_text_centered(DISPLAYSURF)

        if exit_button.get_rect_centered(DISPLAYSURF).collidepoint(mx, my):
            if click:
                pygame.quit()
                sys.exit()
            exit_button.draw_text_centered(DISPLAYSURF, True)
        else:
            exit_button.draw_text_centered(DISPLAYSURF)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        fpsClock.tick(FPS)


player_one = paddle(40, WINDOWHEIGHT/3)
player_two = paddle(WINDOWWIDTH - 70, WINDOWHEIGHT/3)
players = [player_one, player_two]
playing_ball = ball(WINDOWWIDTH/2, WINDOWHEIGHT/2)


def reset_positions():
    player_one.location = pygame.Vector2(40, WINDOWHEIGHT/3)
    player_two.location = pygame.Vector2(WINDOWWIDTH - 70, WINDOWHEIGHT/3)


def game():
    score_one = 0
    score_two = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player_one.velocity = pygame.Vector2(0, PADDLE_VELOCITY)
                if event.key == pygame.K_w:
                    player_one.velocity = pygame.Vector2(0, -PADDLE_VELOCITY)
                if event.key == pygame.K_UP:
                    player_two.velocity = pygame.Vector2(0, -PADDLE_VELOCITY)
                if event.key == pygame.K_DOWN:
                    player_two.velocity = pygame.Vector2(0, PADDLE_VELOCITY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    player_one.velocity = pygame.Vector2(0, 0)
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_two.velocity = pygame.Vector2(0, 0)

        DISPLAYSURF.fill(pygame.Color('black'))
        for player in players:
            player.update()
            player.check_edges(WINDOWHEIGHT=DISPLAYSURF.get_height())
            player.draw(DISPLAYSURF)
            if playing_ball.crect.colliderect(player.rect):
                if playing_ball.oldcrect.left >= player.oldrect.right and playing_ball.crect.left <= player.rect.right:
                    playing_ball.bounce()
                    playing_ball.crect.left = player.rect.right
                if playing_ball.oldcrect.right <= player.oldrect.left and playing_ball.crect.right >= player.rect.left:
                    playing_ball.bounce()
                    playing_ball.crect.right = player.rect.left
                if playing_ball.oldcrect.top >= player.oldrect.bottom and playing_ball.crect.top <= player.rect.bottom:
                    playing_ball.crect.top = player.rect.bottom
                    if playing_ball.velocity.y < 0:
                        playing_ball.velocity.y = -playing_ball.velocity.y
                    else:
                        playing_ball.velocity.y -= 0.1
                if playing_ball.oldcrect.bottom <= player.oldrect.top and playing_ball.crect.bottom >= player.rect.top:
                    playing_ball.velocity.y = -playing_ball.velocity.y
                    playing_ball.crect.bottom = player.rect.top
                pygame.mixer.Sound.play(sound.blip_paddle)
        if playing_ball.crect.left < 0:
            playing_ball.__init__(WINDOWWIDTH/2, WINDOWHEIGHT/2)
            reset_positions()
            score_two += 1
            pygame.mixer.Sound.play(sound.point_beep)
            time.sleep(1)
        if playing_ball.crect.right > WINDOWWIDTH:
            playing_ball.__init__(WINDOWWIDTH/2, WINDOWHEIGHT/2)
            reset_positions()
            score_one += 1
            pygame.mixer.Sound.play(sound.point_beep)
            time.sleep(1)
        gui.draw_text(str(score_one), pong_font, pygame.Color(
            'white'), DISPLAYSURF, WINDOWWIDTH/2 + 20, 20)
        gui.draw_text(str(score_two), pong_font, pygame.Color(
            'white'), DISPLAYSURF, WINDOWWIDTH/2 - 20, 20)
        playing_ball.update()
        playing_ball.check_edges(WINDOWHEIGHT=DISPLAYSURF.get_height())
        playing_ball.draw(DISPLAYSURF)
        fpsClock.tick(FPS)
        pygame.display.update()


def main():
    main_menu()


if __name__ == '__main__':
    main()
