import pygame

from pong_game.config.settings import Settings
from pong_game.objects.player import Player
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class FirstPlayer(Player):
    x_position = 270
    y_position = 510

    image = LoadingImages.PONG_BATS[3]["BAT"]
    angle = 360

    def restart(self):
        self.x = 270
        self.y = 510

    def max_pos(self):
        if self.x <= 200:
            self.x = 200

        if self.x >= 500:
            self.x = 500

        if self.y <= 200:
            self.y = 200

        if self.y >= 880:
            self.y = 880

    def xy_position(self):
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", LoadingImages.SMALL_FONT, "white", 120, 1030,
                         LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"X - ( {round(self.x)} )", LoadingImages.SMALL_FONT, "cyan", 30, 1030,
                         LoadingImages.GAME_SCREEN)

    @staticmethod
    def score():
        DrawUI.draw_text(f"{Settings.f_player_score}", LoadingImages.BIG_FONT, "cyan", 50, 100,
                         LoadingImages.GAME_SCREEN)


