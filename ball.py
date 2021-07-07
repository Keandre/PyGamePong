import pygame
import random
import sound

class ball:
    def __init__(self, x, y):
        self.velocity = pygame.Vector2(
            random.choice([-1, 1]) * random.uniform(3.5, 4.5), random.choice([-1, 1]) * random.uniform(3.5, 4.5))
        self.radius = 7
        self.crect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.oldcrect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.oldcrect.center = self.crect.center
        self.crect.center += self.velocity

    def bounce(self):
        self.velocity.x = -self.velocity.x
        self.velocity.y = random.choice([-1, 1]) * self.velocity.y

    def check_edges(self, WINDOWHEIGHT):
        if self.crect.top <= 0:
            self.crect.top = 0
            self.velocity.y = -self.velocity.y
            pygame.mixer.Sound.play(sound.ball_blip)
        if self.crect.bottom >= WINDOWHEIGHT:
            self.crect.bottom = WINDOWHEIGHT
            self.velocity.y = -self.velocity.y
            pygame.mixer.Sound.play(sound.ball_blip)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255),
                           self.crect.center, self.radius)
        # Only turn on if you want to see the collision box
        #pygame.draw.rect(DISPLAYSURF, (0, 100, 0), self.crect, 1)

