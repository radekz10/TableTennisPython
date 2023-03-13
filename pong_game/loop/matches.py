from pong_game.loop.match_loop import MatchLoop
from pong_game.objects.ball import Ball
from pong_game.objects.first_player import FirstPlayer
from pong_game.objects.second_player import SecondPlayer
from pong_game.ui.loading_images import LoadingImages


class Match:

    @staticmethod
    def f_match():
        MatchLoop.loop(FirstPlayer, SecondPlayer, Ball, LoadingImages.MENU_BACKGROUND[2]["BACKGROUND"],
                       LoadingImages.TABLE[1]["TABLE"], Match.f_match)
