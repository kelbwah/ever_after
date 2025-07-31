import pygame

class Physics:
    def __init__(self):
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration_rate = 650
        self.friction = 0.9
        self.max_speed = 500 