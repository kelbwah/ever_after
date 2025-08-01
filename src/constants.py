import pygame
from enum import Enum

class FontWeight(Enum):
    LIGHT = "./assets/fonts/queensides-light.ttf"
    REGULAR = "./assets/fonts/queensides-regular.ttf"
    MEDIUM = "./assets/fonts/queensides-medium.ttf"
    BOLD = "./assets/fonts/queensides-bold.ttf"

class Constants:
    @staticmethod
    def load_font(font_weight, size):
        if (font_weight == FontWeight.LIGHT):
            return pygame.font.Font(FontWeight.LIGHT.value, size)
        elif (font_weight == FontWeight.REGULAR):
            return pygame.font.Font(FontWeight.REGULAR.value, size)
        elif (font_weight == FontWeight.MEDIUM):
            return pygame.font.Font(FontWeight.MEDIUM.value, size)
        elif (font_weight == FontWeight.BOLD):
            return pygame.font.Font(FontWeight.BOLD.value, size)
        else: 
            raise ValueError("font_weight must be of type enum FontWeight")