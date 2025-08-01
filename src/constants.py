import pygame
from enum import Enum

class FontWeight(Enum):
    LIGHT = "./assets/fonts/queensides-light.ttf"
    REGULAR = "./assets/fonts/queensides-regular.ttf"
    MEDIUM = "./assets/fonts/queensides-medium.ttf"
    BOLD = "./assets/fonts/queensides-bold.ttf"

class FontSize(Enum):
    XS = 16
    SM = 24
    BASE = 36
    LG = 48
    XL = 64
    XXL = 80
    XXXL = 96

class Constants:  
    FONTS = {} 

    @staticmethod
    def load_fonts():
        for weight in FontWeight:
            Constants.FONTS[weight] = {}
            for size in FontSize:
                Constants.FONTS[weight][size] = pygame.font.Font(weight.value, size.value)
        print(Constants.FONTS)


    @staticmethod
    def load_font(font_weight, size):
        return Constants.FONTS[font_weight][size]