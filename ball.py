import pygame
import random
import sounds

class Ball(pygame.sprite.Sprite):
    surface : pygame.Surface
    velocity: pygame.Vector2 = pygame.Vector2(0, 0)
    radius: int
    rect: pygame.Rect
    oldrect: pygame.Rect

    def __init__(self, surface: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.surface = surface
        self.velocity.x = random.choice((-1, 1)) * random.uniform(3.5, 4.5)
        self.velocity.y = random.choice((-1, 1)) * random.uniform(3.5, 4.5)
        self.radius = 7
        self.rect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.oldrect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def bounce(self) -> None:
        self.velocity.x = -self.velocity.x
        self.velocity.y *= random.choice((-1, 1))

    def off_screen(self) -> bool:
        return self.rect.left <= 0 or self.rect.right >= self.surface.get_width()

    def check_edges(self) -> None:
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y *= -1 
            sounds.play("ball_blip.wav")
        if self.rect.bottom >= self.surface.get_height():
            self.rect.bottom = self.surface.get_height() 
            self.velocity.y *= -1
            sounds.play("ball_blip.wav")

    def update(self) -> None:
        pygame.sprite.Sprite.update(self)
        self.oldrect.center = self.rect.center
        self.rect.center += self.velocity
        self.check_edges()

    def draw(self) -> None:
        pygame.draw.circle(self.surface, (255, 255, 255),
                           self.rect.center, self.radius)
        # Only turn on if you want to see the collision box
        #pygame.draw.rect(DISPLAYSURF, (0, 100, 0), self.crect, 1)