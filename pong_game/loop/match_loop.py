import pygame

from pong_game.config.settings import Settings
from pong_game.handler.keybinds import KeyBinds
from pong_game.loop_functions.functions import LoopFunctions, Collisions
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class MatchLoop:
    @staticmethod
    def loop(f_player, s_player, ball, background, table, match_restart):

        pygame.event.set_allowed(pygame.KEYDOWN)

        game_loop = 1

        Settings.countdown = 5
        Settings.last_count = pygame.time.get_ticks()

        while 1:

            clock = pygame.time.Clock()

            f_player = f_player()
            s_player = s_player()

            ball = ball()

            Settings.started = False

            while game_loop:

                clock.tick(Settings.game_tick)

                LoadingImages.GAME_SCREEN.blit(background, (0, 0))
                LoadingImages.GAME_SCREEN.blit(table, (550, 300))

                LoopFunctions.start_countdown(f_player, s_player, ball)

                f_player.render_position(LoadingImages.GAME_SCREEN)
                s_player.render_position(LoadingImages.GAME_SCREEN)

                ball.render_position(LoadingImages.GAME_SCREEN)

                #LoopFunctions.check_show_ui(DrawUI.ui, player_car, car_stopwatch)
                LoopFunctions.check_show_xy(f_player.xy_position)
                LoopFunctions.check_show_xy(s_player.xy_position)
                LoopFunctions.check_show_fps(DrawUI.game_show_fps, clock)

                f_player.score()
                s_player.score()

                ball.out_of_screen()

                LoopFunctions.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                KeyBinds.key_binds(f_player, s_player, match_restart)

                # f_player.max_pos()
                # s_player.max_pos()

                Collisions.check_collisions(f_player, s_player, ball)

            pygame.display.update()
