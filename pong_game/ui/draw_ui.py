from pong_game.ui.loading_images import LoadingImages


class DrawUI:
    @staticmethod
    def draw_text(text, font, color, x, y, game_window):
        set_font = font.render(text, True, color)
        game_window.blit(set_font, (x, y))

    @staticmethod
    def game_show_fps(clock):
        DrawUI.draw_text(f"FPS - {round(clock.get_fps())}", LoadingImages.MEDIUM_FONT, "white", 30, 20,
                         LoadingImages.GAME_SCREEN)
