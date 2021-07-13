import pygame

class Button():
    surface: pygame.Surface
    text: str
    font: pygame.font.Font
    x: int
    y: int
    color: pygame.Color
    hover_color: pygame.Color

    def __init__(self, surface: pygame.Surface, text: str, font: pygame.font.Font, color: pygame.Color, hover_color: pygame.Color, x: int, y: int):
        self.surface = surface
        self.text = text
        self.font = font
        self.x, self.y = (x, y)
        self.color = color
        self.hover_color = hover_color

    def draw_text(self, center=False, hover=False):
        text_obj = self.font.render(
            self.text, 1, self.color if not hover else self.hover_color)
        
        if center:
            text_rect = text_obj.get_rect(center=(self.surface.get_width() // 2, self.y))
        else:
            text_rect = text_obj.get_rect()
            text_rect.topleft = (self.x, self.y)

        self.surface.blit(text_obj, text_rect)

    def get_rect(self, center=False):
        text_obj = self.font.render(
            self.text, 1, self.color)
        if center:
            return text_obj.get_rect(center=(self.surface.get_width() // 2, self.y))
        else:
            text_rect = text_obj.get_rect()
            text_rect.topleft = (self.x, self.y)
            return text_rect

def draw_text(surface: pygame.Surface, text: str, font: pygame.font.Font, color: pygame.Color, x : int, y : int, center=False):
    text_obj = font.render(text, 1, color)
    if center:
        text_rect = text_obj.get_rect(center=(surface.get_width() // 2, y))
    else:
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)