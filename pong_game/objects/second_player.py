from pong_game.config.settings import Settings
from pong_game.objects.player import Player
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class SecondPlayer(Player):
    x_position = 1585
    y_position = 510

    image = LoadingImages.PONG_BATS[4]["BAT"]
    angle = 360

    def max_pos(self):
        if self.x >= 1720:
            self.x = 1720

        if self.x <= 1420:
            self.x = 1420

        if self.y <= 200:
            self.y = 200

        if self.y >= 880:
            self.y = 880

    def xy_position(self):
        DrawUI.draw_text(f"X - ( {round(self.x)} )", LoadingImages.SMALL_FONT, "white", 1720, 1030,
                         LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", LoadingImages.SMALL_FONT, "cyan", 1810, 1030,
                         LoadingImages.GAME_SCREEN)

    @staticmethod
    def score():
        DrawUI.draw_text(f"Score - {Settings.s_player_score}", LoadingImages.MEDIUM_FONT, "light blue", 1750, 100,
                         LoadingImages.GAME_SCREEN)
