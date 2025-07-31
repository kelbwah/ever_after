import pygame
from game import Game
from scenes.SceneManager import SceneManager
from settings import Settings
from physics import Physics
from assets import Assets

if __name__ == "__main__":
    pygame.init()
    game = Game(
        SceneManager(), 
        Settings(), 
        Physics(),
        Assets()
    )
    game.run()
