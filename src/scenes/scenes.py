from enum import Enum
from .main_menu_screen import MainMenuScreen
import pygame

# initialize fonts for all scenes
pygame.font.init()

class Scenes(Enum):
    INTRO = 'intro'
    MAIN_MENU = "main_menu"
    PAUSED = "paused"
    SETTINGS = "settings"
    ACT_1 = "act_1"
    ACT_2 = "act_2"
    ACT_3 = "act_3"
    ACT_4 = "act_4"

SCENE_MAP = {
    Scenes.INTRO: 'intro',
    Scenes.MAIN_MENU: MainMenuScreen,
    Scenes.PAUSED: "paused",
    Scenes.SETTINGS: "settings",
    Scenes.ACT_1: "act_1",
    Scenes.ACT_2: "act_2",
    Scenes.ACT_3: "act_3",
    Scenes.ACT_4: "act_4",
}