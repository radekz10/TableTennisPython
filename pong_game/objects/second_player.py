from pong_game.config.settings import Settings
from pong_game.objects.player import Player
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class SecondPlayer(Player):
    x_position = 1400
    y_position = 540

    image = LoadingImages.PONG_BATS[2]["BAT"]
    angle = 360

    def max_pos(self):
        if self.x >= 1550:
            self.x = 1550

        if self.x <= 1300:
            self.x = 1300

        if self.y <= 280:
            self.y = 280

        if self.y >= 680:
            self.y = 680

    def xy_position(self):
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", LoadingImages.SMALL_FONT, "white", 1720, 1030,
                         LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"X - ( {round(self.x)} )", LoadingImages.SMALL_FONT, "cyan", 1810, 1030,
                         LoadingImages.GAME_SCREEN)

    @staticmethod
    def score():
        DrawUI.draw_text(f"Score - {Settings.s_player_score}", LoadingImages.MEDIUM_FONT, "light blue", 1750, 200,
                         LoadingImages.GAME_SCREEN)
