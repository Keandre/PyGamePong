from pygame.locals import *
from paddle import Paddle
from ball import Ball
import pygame
import sys
import time
import sounds
import gui
import fonts
pygame.init()

WINDOWWIDTH, WINDOWHEIGHT = 600, 600
WINDOW_DIMENSIONS = (WINDOWWIDTH, WINDOWHEIGHT)
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_DIMENSIONS, 0, 32)
PADDLE_VELOCITY = 7

font = fonts.make_font("Georgia.ttf", 20)
pong_font = fonts.make_font("bit5x3.ttf", 30)
pong_font_title = fonts.make_font("bit5x3.ttf", 30)

player_one = Paddle(DISPLAYSURF, 40, WINDOWHEIGHT // 3)
player_two = Paddle(DISPLAYSURF, WINDOWWIDTH - 70, WINDOWHEIGHT // 3)
ball = Ball(DISPLAYSURF, WINDOWWIDTH // 2, WINDOWHEIGHT // 2)

players = pygame.sprite.Group()
players.add(player_one)
players.add(player_two)


def reset_positions():
    player_one.rect.topleft = pygame.Vector2(40, WINDOWHEIGHT/3)
    player_two.rect.topleft = pygame.Vector2(WINDOWWIDTH - 70, WINDOWHEIGHT/3)

def draw_scores(score_one : str, score_two : str, spacing : int):
    gui.draw_text(DISPLAYSURF, str(score_one), pong_font, pygame.Color('white'), WINDOWWIDTH // 2 - spacing, 20)
    gui.draw_text(DISPLAYSURF, str(score_two), pong_font, pygame.Color('white'), WINDOWWIDTH // 2 + spacing, 20)

def main_menu():
    while True:
        DISPLAYSURF.fill(pygame.Color('black'))
        gui.draw_text(DISPLAYSURF, 'PONG', pong_font_title, pygame.Color('white'), 0, 50, center=True)

        play_button = gui.Button(DISPLAYSURF, 'PLAY', pong_font, pygame.Color('white'), pygame.Color('yellow'), 0, 150)
        exit_button = gui.Button(DISPLAYSURF, 'EXIT', pong_font, pygame.Color('white'), pygame.Color('yellow'), 0, 210)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_button.get_rect(center=True).collidepoint(mouse_x, mouse_y):
            if click:
                sounds.play("menu_click.wav")
                game()
            play_button.draw_text(center=True, hover=True)
        else:
            play_button.draw_text(center=True, hover=False)

        if exit_button.get_rect(center=True).collidepoint(mouse_x, mouse_y):
            if click:
                pygame.quit()
                sys.exit()
            exit_button.draw_text(center=True, hover=True)
        else:
            exit_button.draw_text(center=True, hover=False)

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
            if ball.rect.colliderect(player.rect):
                if ball.oldrect.left >= player.oldrect.right and ball.rect.left <= player.rect.right:
                    ball.bounce()
                    ball.rect.left = player.rect.right
                if ball.oldrect.right <= player.oldrect.left and ball.rect.right >= player.rect.left:
                    ball.bounce()
                    ball.rect.right = player.rect.left
                if ball.oldrect.top >= player.oldrect.bottom and ball.rect.top <= player.rect.bottom:
                    ball.rect.top = player.rect.bottom
                    if ball.velocity.y < 0:
                        ball.velocity.y *= -1 
                    else:
                        ball.velocity.y -= 0.1
                if ball.oldrect.bottom <= player.oldrect.top and ball.rect.bottom >= player.rect.top:
                    ball.velocity.y = -ball.velocity.y
                    ball.rect.bottom = player.rect.top
                sounds.play("blip_paddle.wav")

        if ball.off_screen():
            reset_positions()
            sounds.play("point_beep.wav")
            time.sleep(1)
            if ball.rect.left <= 0:
                score_two += 1
            else:
                score_one += 1
            ball.rect.center = WINDOWWIDTH // 2, WINDOWHEIGHT // 2

        for player in players:
            player.draw()
        players.update()

        ball.update()
        ball.draw()

        draw_scores(score_one, score_two, 30)
        fpsClock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main_menu()