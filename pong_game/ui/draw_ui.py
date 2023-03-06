
class DrawUI:
    @staticmethod
    def draw_text(text, font, color, x, y, game_window):
        set_font = font.render(text, True, color)
        game_window.blit(set_font, (x, y))
