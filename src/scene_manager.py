from scenes import scenes

class SceneManager:
    def __init__(self):
        self.current_scene = scenes.Scenes.MAIN_MENU.value
        self.game = None
    
    def set_scene(self, scene):
        self.current_scene = scene
    
    def get_scene(self):
        return self.current_scene
    
    def load_scene(self):
        if not self.game:
            raise ValueError("self.game is None")

        self.current_scene.draw_screen(self.game.resource_manager, self.game.screen_manager)
        self.current_scene.handle_events()
    
    def set_game(self, game):
        self.game = game