import pygame

from pong_game.config.settings import Settings
from pong_game.handler.keybinds import KeyBinds
from pong_game.loop_functions.functions import LoopFunctions
from pong_game.ui.loading_images import LoadingImages


class MatchLoop:
    @staticmethod
    def loop(f_player, s_player, background, table, match_restart):

        pygame.event.set_allowed(pygame.KEYDOWN)

        game_loop = 1

        Settings.countdown = 5
        Settings.last_count = pygame.time.get_ticks()

        while 1:

            clock = pygame.time.Clock()

            #f_player = f_player()
            #s_player = s_player()

            Settings.started = False

            while game_loop:

                clock.tick(Settings.game_tick)

                LoadingImages.GAME_SCREEN.blit(background, (0, 0))
                LoadingImages.GAME_SCREEN.blit(table, (0, 0))

                LoopFunctions.start_countdown(f_player, s_player)

                LoopFunctions.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                KeyBinds.f_player_key_binds(f_player, match_restart)
                KeyBinds.s_player_key_binds(s_player, match_restart)

            pygame.display.update()
