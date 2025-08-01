import pygame
from constants import Constants

class ResourceManager:
    def __init__(self):
        self.bg_images = []
        
    def load_assets(self):
        self.load_bg_images()
        Constants.load_fonts()

    def load_bg_images(self):
        for i in range(1, 10):
            bg_image = pygame.image.load(f"assets/backgrounds_new/PNG/game_background_2/layers/{i}.png").convert_alpha()
            scaled_image = pygame.transform.scale(bg_image, (1280, 720))
            self.bg_images.append(scaled_image)