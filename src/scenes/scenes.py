from enum import Enum
from .main_menu_screen import MainMenuScreen
import pygame

# initialize fonts for all scenes
pygame.font.init()

class Scenes(Enum):
    INTRO = 'intro'
    MAIN_MENU = MainMenuScreen()
    PAUSED = "paused"
    SETTINGS = "settings"
    ACT_1 = "act_1"
    ACT_2 = "act_2"
    ACT_3 = "act_3"
    ACT_4 = "act_4"