from pong_game.config.settings import Settings
from pong_game.objects.player import Player
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class FirstPlayer(Player):
    x_position = 450
    y_position = 540

    image = LoadingImages.PONG_BATS[1]["BAT"]
    angle = 360

    def max_pos(self):
        if self.x >= 600:
            self.x = 600

    def xy_position(self):
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", LoadingImages.SMALL_FONT, "white", 120, 1030,
                         LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"X - ( {round(self.x)} )", LoadingImages.SMALL_FONT, "cyan", 30, 1030,
                         LoadingImages.GAME_SCREEN)

    @staticmethod
    def score():
        DrawUI.draw_text(f"Score - {Settings.f_player_score}", LoadingImages.MEDIUM_FONT, "light blue", 50, 200,
                         LoadingImages.GAME_SCREEN)
