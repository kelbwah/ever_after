from constants import FontWeight, FontSize
from config import Config
import components.text as text

class UI:
    @staticmethod
    def render_ui(screen_manager):
        UI.show_fps(Config.load_settings(), screen_manager)

    @staticmethod
    def show_fps(settings, screen_manager):
        if (settings["SHOW_FPS"]):
            fps_text_surface = text.create_text_surface(FontWeight.REGULAR, FontSize.BASE, f"{str(screen_manager.get_fps())[0:2]}", (50, 55, 60))
            text.render_text(screen_manager.screen, fps_text_surface, (10, 0))