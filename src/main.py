import pygame
from game import Game
from services.screen_manager import ScreenManager
from services.resource_manager import ResourceManager
from services.scene_manager import SceneManager

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Ever After")

    screen_manager = ScreenManager()
    resource_manager = ResourceManager()
    scene_manager = SceneManager()

    game = Game(screen_manager, resource_manager, scene_manager)

    scene_manager.set_game(game)
    resource_manager.load_assets()

    game.run()