from constants import Constants, FontWeight
import text

class MainMenuScreen:
    def __init__(self): 
        self.scroll = 0

    def draw_screen(self, game):
        self.scroll += 0.5
        self.draw_bg(game)

        text.render_text(game.screen, FontWeight.MEDIUM, 72, "Ever After", (255, 255, 255), (90, 60))
        text.render_text(game.screen, FontWeight.REGULAR, 28, "A journey through love.", (255, 255, 255), (90, 150))
        text.render_text(game.screen, FontWeight.MEDIUM, 36, f"{str(game.clock.get_fps())[0:2]}", (255, 255, 255), (10, 0))
    
    def draw_bg(self, game):
        for i, img in (enumerate(reversed(game.assets.bg_images))):
            speed = 1 + i * 0.2
            bg_width = img.get_width()
            scroll_x = (self.scroll * speed) % bg_width

            game.screen.blit(img, (-scroll_x, 0))
            game.screen.blit(img, (bg_width - scroll_x, 0))

    
    def handle_events(self):
        pass