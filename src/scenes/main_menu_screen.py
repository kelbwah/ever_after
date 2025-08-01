import components.text as text
from constants import FontWeight, FontSize
from services.ui_manager import UI

class MainMenuScreen():
    def __init__(self):
        self.bg_offset_speed = 1 # the offset that is added to each bg layer's speed for a bg parallax effect
        self.scroll = 0
        self.text_color = (50, 55, 60)

    def draw_screen(self, resource_manager, screen_manager):
        self.draw_bg(resource_manager, screen_manager)
        UI.render_ui(screen_manager)

        text.render_text(screen_manager.screen, FontWeight.BOLD, FontSize.XXL, "Ever After", self.text_color, (90, 60))
        text.render_text(screen_manager.screen, FontWeight.MEDIUM, FontSize.SM, "A journey through love.", self.text_color, (90, 165))
    
    def draw_bg(self, resource_manager, screen_manager):
        self.scroll += 0.1
        for i, img in (enumerate(reversed(resource_manager.bg_images))):
            speed = 1 + i * self.bg_offset_speed
            bg_width = img.get_width()
            scroll_x = (self.scroll * speed) % bg_width

            screen_manager.screen.blit(img, (-scroll_x, 0))
            screen_manager.screen.blit(img, (bg_width - scroll_x, 0))
    
    def handle_events(self):
        pass