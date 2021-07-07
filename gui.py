import pygame 

class button:
    def __init__(self, text, font, color, hover_color, x, y):
        self.text = text
        self.font = font
        self.x, self.y = (x,y)
        self.color = color
        self.hover_color = hover_color

    def draw_text(self, surface, hover=False):
        textobj = self.font.render(self.text, 1, self.color if not hover else self.hover_color)
        text_rect = textobj.get_rect()
        text_rect.topleft = (self.x,self.y)
        surface.blit(textobj, text_rect)
    
    def draw_text_centered(self, surface, hover=False):
        textobj = self.font.render(self.text, 1, self.color if not hover else self.hover_color)
        text_rect = textobj.get_rect(center=(surface.get_width()//2, self.y))
        surface.blit(textobj, text_rect)

    def get_rect_centered(self, surface): 
        return self.font.render(self.text, 1, self.color).get_rect(center=(surface.get_width()//2, self.y))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(textobj, text_rect)    

 
def draw_text_center(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_rect = textobj.get_rect(center=(surface.get_width()//2, y))
    surface.blit(textobj, text_rect)      

