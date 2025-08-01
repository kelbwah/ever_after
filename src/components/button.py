import pygame
from enum import Enum

class ButtonStates(Enum):
    IDLE = 1
    HOVER = 2
    ACTIVE = 3

class Button():
    def __init__(self, position, text, text_color, background_color, radius):
        self.position = position 
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.radius = radius
        self.radius = radius
        self.current_state = ButtonStates.IDLE

    def handle_button_events():
        pass

    def on_mouse_press(self):
        pass 

    def on_mouse_release(self):
        self.initiate_action()

    def initiate_action(self):
        pass