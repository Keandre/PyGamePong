import pygame

class paddle:
    def __init__(self, x, y):
        self.location = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.paddle_width, self.paddle_height = 30, 150
        self.rect = pygame.Rect(
            self.location.x, self.location.y, self.paddle_width, self.paddle_height)
        self.oldrect = pygame.Rect(
            self.location.x, self.location.y, self.paddle_width, self.paddle_height)

    def update(self):
        self.oldrect = self.rect
        self.location += self.velocity

    def check_edges(self, WINDOWHEIGHT):
        if self.location.y < 0:
            self.velocity.y, self.location.y = 0, 0
        if self.location.y + self.paddle_height > WINDOWHEIGHT:
            self.location.y = WINDOWHEIGHT - self.paddle_height
            self.velocity.y = 0

    def draw(self, surface):
        self.rect = pygame.Rect(
            self.location.x, self.location.y, self.paddle_width, self.paddle_height)
        pygame.draw.rect(surface, pygame.Color(255, 255, 255), self.rect)