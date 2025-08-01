import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)