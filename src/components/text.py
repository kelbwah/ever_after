from constants import Constants

def render_text(screen, font_weight, size, text, color, coordinates):
    text_surface = Constants.load_font(font_weight, size).render(text, True, color)
    screen.blit(text_surface, coordinates)