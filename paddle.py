import pygame


class Paddle(pygame.sprite.Sprite):
    surface: pygame.Surface
    velocity: pygame.Vector2
    paddle_width: int
    paddle_height: int
    rect: pygame.Rect
    oldrect: pygame.Rect

    def __init__(self, surface: pygame.Surface, x: int, y: int) -> None:
        super().__init__()
        self.surface = surface
        self.velocity = pygame.Vector2(0, 0)
        self.paddle_width, self.paddle_height = 30, 150
        self.rect = pygame.Rect(
            x, y, self.paddle_width, self.paddle_height)
        self.oldrect = pygame.Rect(
            x, y, self.paddle_width, self.paddle_height)

    def check_edges(self) -> None:
        if self.rect.top < 0:
            self.velocity.y = 0
            self.rect.top = 0
        if self.rect.bottom > self.surface.get_height():
            self.rect.bottom = self.surface.get_height()
            self.velocity.y = 0

    def update(self) -> None:
        pygame.sprite.Sprite.update(self)
        self.check_edges()
        self.oldrect = self.rect
        self.rect.topleft += self.velocity

    def draw(self) -> None:
        pygame.draw.rect(self.surface, pygame.Color(255, 255, 255), self.rect)
