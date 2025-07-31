from scenes import scenes

class SceneManager:
    def __init__(self):
        self.current_scene = scenes.Scenes.MAIN_MENU.value
    
    def set_scene(self, scene):
        self.current_scene = scene
    
    def get_scene(self):
        return self.current_scene
    
    def load_scene(self, game):
        self.current_scene.draw_screen(game)
        self.current_scene.handle_events()