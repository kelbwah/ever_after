import pygame

class Game:
    def __init__(self, scene_manager, settings, physics, assets):
        self.scene_manager = scene_manager 
        self.physics = physics
        self.settings = settings
        self.assets = assets
        self.is_running = True
        self.is_paused = False 
        self.display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.dt = 0

    def run(self):
        pygame.display.set_caption("Ever After")
        self.assets.load_assets()
     
        while self.is_running:
            self.dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            self.scene_manager.load_scene(self)

            pygame.display.flip()
        
        pygame.quit()