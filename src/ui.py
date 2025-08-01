from constants import FontWeight
from config import Config
import text

class UI:
    @staticmethod
    def render_ui(screen_manager):
        UI.show_fps(Config.load_settings(), screen_manager)

    @staticmethod
    def show_fps(settings, screen_manager):
        if (settings["SHOW_FPS"]):
            text.render_text(screen_manager.screen, FontWeight.REGULAR, 36, f"{str(screen_manager.get_fps())[0:2]}", (50, 55, 60), (10, 0))