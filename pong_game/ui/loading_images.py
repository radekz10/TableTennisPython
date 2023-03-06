import pygame

from pong_game.config.settings import Settings

pygame.init()


class LoadingImages:
    WIDTH = 1920
    HEIGHT = 1080
    FLAGS = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    GAME_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, 16, vsync=Settings.vsync)

    @staticmethod
    def res(image, amount):
        new_res = (image.get_width() * amount), (image.get_height() * amount)

        return pygame.transform.scale(image, new_res)

    @staticmethod
    def res_width(image, amount):
        new_res = (image.get_width() * amount)

        return pygame.transform.scale(image, new_res)

    @staticmethod
    def res_height(image, amount):
        new_res = (image.get_height() * amount)

        return pygame.transform.scale(image, new_res)

    # BACKGROUNDS -----------------------------------------------------------------------------------------------------

    MENU_BACKGROUND = {

        1: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/wallpaper.jpg"), 0.75).convert_alpha()},

    }

    BUTTONS = {

        1: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1).convert_alpha()},
        2: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1.3).convert_alpha()},

        3: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button.png"), 1).convert_alpha()},
        4: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_win_lose.png"), 1.5).convert_alpha()},

        5: {"BUTTON": res(pygame.image.load("../images/ui/buttons/settings_button.png"), 0.1).convert_alpha()},
        6: {"BUTTON": res(pygame.image.load("../images/ui/buttons/binds_button.png"), 0.15).convert_alpha()}

    }

    # FONTS -----------------------------------------------------------------------------------------------------------

    NORMAL_FONT = pygame.font.SysFont("impact", 60)
    SMALL_FONT = pygame.font.SysFont("impact", 20)
    BIG_FONT = pygame.font.SysFont("impact", 100)
    MEDIUM_FONT = pygame.font.SysFont("impact", 35)
