from pong_game.objects.player import Player
from pong_game.ui.loading_images import LoadingImages


class SecondPlayer(Player):

    x_position = 1500
    y_position = 540

    image = LoadingImages.PONG_BATS[2]["BAT"]
    angle = 360
