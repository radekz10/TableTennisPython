from pong_game.storage.data_processing import DataProcessing


class Settings:
    started = False

    # tick
    game_tick = 60

    # countdown
    countdown = 5
    last_count = 0

    # on - 1 / off - 2
    audio = 1
    vsync = 1
    show_fps = 1
    show_xy = 1

    start_time = 0

    f_player_score = 0
    s_player_score = 0

    FILE_PATHS = {

        1: {"FILE": "../pong_game/storage/files/wins.txt"},
    }

    win_file = DataProcessing.load_wins(FILE_PATHS[1]["FILE"])

    win_coins = int(win_file[len(win_file) - 1])
    # win_coins = 30
    # print(win_coins)