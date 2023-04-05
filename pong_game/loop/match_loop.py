from random import randint

import pygame

from pong_game.config.settings import Settings
from pong_game.handler.keybinds import KeyBinds
from pong_game.loop_functions.functions import LoopFunctions, Collisions
from pong_game.sounds.sounds import Sounds
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class MatchLoop:
    @staticmethod
    def loop(f_player, s_player, ball, background, table, match_restart):

        pygame.event.set_allowed(pygame.KEYDOWN)

        Settings.f_player_score = 0
        Settings.s_player_score = 0

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

                # LoopFunctions.check_show_ui(DrawUI.ui, player_car, car_stopwatch)
                LoopFunctions.check_show_xy(f_player.xy_position)
                LoopFunctions.check_show_xy(s_player.xy_position)
                LoopFunctions.check_show_fps(DrawUI.game_show_fps, clock)

                f_player.score()
                s_player.score()

                #if ball.x <= 500 or ball.x >= 1450:
                    #ball.x *= -1
                    #Sounds.ball_hit.play()
                    # self.y = 500
                #if ball.y <= 300 or ball.y >= 800:
                    #ball.y *= -1
                    #Sounds.ball_hit.play()

                if f_player.get_rect().colliderect(ball.get_rect()):
                    ball.speed *= -1
                    #ball.x += ball.speed
                    #ball.y += ball.speed / 2
                    Sounds.bat_ball_hit.play()

                if s_player.get_rect().colliderect(ball.get_rect()):
                    ball.speed *= -1
                    #ball.x += ball.speed
                    #ball.y += ball.speed / 2
                    Sounds.bat_ball_hit.play()

                if ball.y >= LoadingImages.GAME_SCREEN.get_height() or ball.y <= 0:
                    ball.speed *= -1
                    Sounds.ball_hit.play()

                if ball.x >= LoadingImages.GAME_SCREEN.get_width() or ball.x <= 0:
                    ball.speed *= -1
                    Sounds.ball_hit.play()


                # if ball.x <= 500 or ball.x >= 1450:
                # ball.x *= -1

                #if ball.x < 500:
                    # ball.x = 700
                    # ball.respawn()
                    #Settings.f_player_score += 1

                #if ball.x > 1450:
                    # ball.respawn()
                    #Settings.s_player_score += 1

                #if ball.x < 200:
                    #ball.respawn()

                #if ball.x > 1850:
                    #ball.respawn()

                    # self.y = 500
                # if ball.y <= 0 or ball.y >= 1080:
                # ball.y = 700

                # ball.out_of_screen()

                #Collisions.check_ball_pos(ball)
                # Collisions.check_score(match_restart)

                # ball.ball_pos()

                # Collisions.col(ball)

                LoopFunctions.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                KeyBinds.key_binds(f_player, s_player, match_restart)

                # f_player.max_pos()
                # s_player.max_pos()

                # Collisions.check_collisions(f_player, s_player, ball)

            pygame.display.update()
