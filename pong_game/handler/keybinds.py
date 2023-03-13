import pygame

import pong_game.ui.menu

class KeyBinds:
    @staticmethod
    def f_player_key_binds(f_player, match_restart):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_w]:
            f_player.forward_control()

        else:
            f_player.forward_slowdown()

        if pressed_key[pygame.K_s]:
            f_player.backward_control()
        else:
            f_player.forward_slowdown()

        if pressed_key[pygame.K_d]:
            f_player.rotate_right()

        if pressed_key[pygame.K_a]:
            f_player.rotate_left()

        if pressed_key[pygame.K_x]:
            pong_game.ui.menu.Menu.main_menu()

        if pressed_key[pygame.K_r]:
            match_restart()

    @staticmethod
    def s_player_key_binds(s_player, match_restart):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_i]:
            s_player.forward_control()
        else:
            s_player.forward_slowdown()

        if pressed_key[pygame.K_k]:
            s_player.backward_control()
        else:
            s_player.forward_slowdown()

        if pressed_key[pygame.K_l]:
            s_player.rotate_right()

        if pressed_key[pygame.K_j]:
            s_player.rotate_left()

        if pressed_key[pygame.K_r]:
            match_restart()
