import pygame

import pong_game.ui.menu
from pong_game.loop_functions.functions import LoopFunctions
from pong_game.sounds.sounds import Sounds


class KeyBinds:
    @staticmethod
    def f_player_key_binds(f_player, match_restart):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_w]:
            f_player.up()

        if pressed_key[pygame.K_s]:
            f_player.down()

        if pressed_key[pygame.K_d]:
            f_player.right()

        if pressed_key[pygame.K_a]:
            f_player.left()

        if pressed_key[pygame.K_q]:
            f_player.rotate_left()

        if pressed_key[pygame.K_e]:
            f_player.rotate_right()

        if pressed_key[pygame.K_x]:
            LoopFunctions.stop_audio()
            pong_game.ui.menu.Menu.main_menu()

        if pressed_key[pygame.K_r]:
            LoopFunctions.stop_audio()
            match_restart()

    @staticmethod
    def s_player_key_binds(s_player, match_restart):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_i]:
            s_player.up()

        if pressed_key[pygame.K_k]:
            s_player.down()

        if pressed_key[pygame.K_j]:
            s_player.left()

        if pressed_key[pygame.K_l]:
            s_player.right()

        if pressed_key[pygame.K_r]:
            LoopFunctions.stop_audio()
            match_restart()

    @staticmethod
    def key_binds(f_player, s_player, match_restart):
        KeyBinds.f_player_key_binds(f_player, match_restart)
        KeyBinds.s_player_key_binds(s_player, match_restart)
