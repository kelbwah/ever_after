import pygame
from config import Config

class ScreenManager:
    def __init__(self):
        self.dt = 0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Config.get_setting("WINDOW_WIDTH"), Config.get_setting("WINDOW_HEIGHT")))
    
    def get_fps(self):
        return self.clock.get_fps()