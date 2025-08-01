import pygame

class Game():
    def __init__(self, screen_manager, resource_manager, scene_manager):
        self.screen_manager = screen_manager 
        self.resource_manager = resource_manager
        self.scene_manager = scene_manager
        self.is_running = True
    
    def run(self):
        pygame.display.set_caption("Ever After")
        self.resource_manager.load_assets()

        while self.is_running:
            self.screen_manager.dt = self.screen_manager.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            self.scene_manager.load_scene()

            pygame.display.flip()
        
        pygame.quit()