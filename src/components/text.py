from constants import Constants

def create_text_surface(font_weight, size, text, color):
    text_surface = Constants.load_font(font_weight, size).render(text, True, color)
    return text_surface


def render_text(screen, text_surface, coordinates):
    screen.blit(text_surface, coordinates)