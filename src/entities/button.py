import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, name, text):
        self.name = name
        self.position = (0, 0)
        self.text = text

    def on_mouse_press(self):
        pass

    def on_mouse_release(self):
        pass

    def start_action(self):
        pass