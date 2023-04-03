import pygame

from pong_game.config.settings import Settings

pygame.init()


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


def res_width(image, amount):
    new_res = (image.get_width() * amount), (image.get_height())

    return pygame.transform.scale(image, new_res)


def res_height(image, amount):
    new_res = (image.get_width()), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


class LoadingImages:
    WIDTH = 1920
    HEIGHT = 1080
    FLAGS = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    GAME_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, 16, vsync=Settings.vsync)

    # ICONS ------------------------------------------------------------------------------------------------------------
    trophy_icon = res(pygame.image.load("../images/icons/trophy-icon.png"), 0.2).convert_alpha()
    star_icon = res(pygame.image.load("../images/icons/star_icon.png"), 0.2).convert_alpha()

    # FONTS ------------------------------------------------------------------------------------------------------------
    NORMAL_FONT = pygame.font.SysFont("impact", 60)
    SMALL_FONT = pygame.font.SysFont("impact", 20)
    BIG_FONT = pygame.font.SysFont("impact", 100)
    MEDIUM_FONT = pygame.font.SysFont("impact", 35)

    # BACKGROUNDS ------------------------------------------------------------------------------------------------------

    MENU_BACKGROUND = {

        1: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/wallpaper.jpg"), 0.75).convert_alpha()},
        2: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/grey_wallpaper.jpg"), 1).convert_alpha()},
        3: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/wallpaper_light.jpg"), 1).convert_alpha()},
        4: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/time_background3.png"), 1).convert_alpha()}

    }

    TABLE = {

        1: {"TABLE": res(pygame.image.load("../images/ui/table/pong_table2.png"), 1.5).convert_alpha()},
        2: {"TABLE": res(pygame.image.load("../images/ui/table/pong_table2.png"), 1.8).convert_alpha()},

    }

    PONG_BATS = {

        1: {"BAT": res(pygame.image.load("../images/ui/bat/bat2.png"), 0.1).convert_alpha()},
        2: {"BAT": res(pygame.image.load("../images/ui/bat/bat3.png"), 0.1).convert_alpha()},

    }

    PONG_BALL = {

        1: {"BALL": res(pygame.image.load("../images/ui/ball/pong_ball.png"), 0.025).convert_alpha()}

    }

    # BUTTONS ----------------------------------------------------------------------------------------------------------

    BUTTONS = {

        1: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1).convert_alpha()},
        2: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1.3).convert_alpha()},

        3: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button.png"), 1).convert_alpha()},
        #4: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_win_lose.png"), 1.5).convert_alpha()},

        5: {"BUTTON": res(pygame.image.load("../images/ui/buttons/settings_button.png"), 0.1).convert_alpha()},
        6: {"BUTTON": res(pygame.image.load("../images/ui/buttons/binds_button.png"), 0.15).convert_alpha()}

    }

    ON_OFF_BUTTONS = {

        1: {"BUTTON": res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 1).convert_alpha()},
        2: {"BUTTON": res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 2).convert_alpha()}

    }
