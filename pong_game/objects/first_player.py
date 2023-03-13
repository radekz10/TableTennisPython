from pong_game.objects.player import Player
from pong_game.ui.loading_images import LoadingImages


class FirstPlayer(Player):

    x_position = 450
    y_position = 540

    image = LoadingImages.PONG_BATS[1]["BAT"]
    angle = 360
