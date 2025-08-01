import pygame
from screen_manager import ScreenManager
from resource_manager import ResourceManager
from scene_manager import SceneManager
from game import Game

if __name__ == "__main__":
    pygame.init()

    screen_manager = ScreenManager()
    resource_manager = ResourceManager()
    scene_manager = SceneManager()

    game = Game(screen_manager, resource_manager, scene_manager)
    scene_manager.set_game(game)

    game.run()

