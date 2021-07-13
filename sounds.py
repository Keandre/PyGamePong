import pygame
import os
pygame.mixer.init()

SOUND_PATH = os.path.join("sound/")

def play(file_name : str, path=SOUND_PATH) -> None:
    sound = pygame.mixer.Sound(path + file_name)
    pygame.mixer.Sound.play(sound)

