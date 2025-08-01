import pygame
from enum import Enum

class ButtonStates(Enum):
    IDLE = 1
    HOVER = 2
    ACTIVE = 3

class Button():
    def __init__(self, name, text):
        self.name = name
        self.position = (0, 0)
        self.text = text
        self.current_state = ButtonStates.IDLE

    def on_mouse_press(self):
        pass

    def on_mouse_release(self):
        self.initiate_action()

    def initiate_action(self):
        pass