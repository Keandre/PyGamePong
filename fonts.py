import pygame
import os 

FONT_PATH = os.path.join("fonts/")

def make_font(file_name : str, font_size : int, path=FONT_PATH):
    return pygame.font.Font(path + file_name, font_size)
