from random import randint

import pygame

from pong_game.config.settings import Settings
from pong_game.sounds.sounds import Sounds
from pong_game.storage.data_processing import DataProcessing
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class LoopFunctions:

    @staticmethod
    def check_new_game():
        Settings.started = False

        while not Settings.started:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[4]["BACKGROUND"], (700, 200))
            DrawUI.draw_text("PLAY AGAIN - SPACE", LoadingImages.NORMAL_FONT, "white", 740, 250,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("EXIT TO MENU - X", LoadingImages.NORMAL_FONT, "cyan", 740, 350, LoadingImages.GAME_SCREEN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Settings.started = 1
                    # Match.f_match()

    @staticmethod
    def start_game():
        while not Settings.started:
            DrawUI.draw_text(f"PRESS ANY KEY TO START", LoadingImages.MEDIUM_FONT, "orange", 800, 600,
                             LoadingImages.GAME_SCREEN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Settings.started = 1

    @staticmethod
    def start_countdown(f_player, s_player, ball):
        x = LoadingImages.GAME_SCREEN.get_width() / 2
        y = LoadingImages.GAME_SCREEN.get_height() / 2

        color = "white"

        if Settings.countdown > 0:

            count_timer = pygame.time.get_ticks()

            f_player.max_speed = 0
            f_player.speed = 0

            s_player.max_speed = 0
            s_player.speed = 0

            if count_timer - Settings.last_count > 1000:
                Settings.countdown -= 1
                Settings.last_count = count_timer

        if Settings.countdown == 5:
            DrawUI.draw_text(f"{str(Settings.countdown)}", LoadingImages.BIG_FONT, "white", x, y,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 4:
            LoopFunctions.check_audio(Sounds.countdown.play)
            DrawUI.draw_text(f"{str(Settings.countdown)}", LoadingImages.BIG_FONT, "lime", x, y,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 3:
            DrawUI.draw_text(f"{str(Settings.countdown)}", LoadingImages.BIG_FONT, "lime", x, y,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 2:
            DrawUI.draw_text(f"{str(Settings.countdown)}", LoadingImages.BIG_FONT, "cyan", x, y,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 1:
            DrawUI.draw_text(f"{str(Settings.countdown)}", LoadingImages.BIG_FONT, "cyan", x, y,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown <= 0:
            f_player.speed = 10
            s_player.speed = 10

            # ball.movement()
            # ball.x += 1
            # ball.x += ball.speed
            # ball.y += ball.speed

            #ball.movement()
            # ball.y += ball.speed / 2

            # ball.x += randint(5, 10)
            # ball.y += randint(5, 10) / 2

    @staticmethod
    def check_show_fps(command, clock):
        if Settings.show_fps == 1:
            command(clock)

    @staticmethod
    def check_show_xy(command):
        if Settings.show_xy == 1:
            command()

    @staticmethod
    def check_audio(command):
        if Settings.audio == 1:
            command()


class Collisions:
    @staticmethod
    def f_player_vs_ball(f_player, ball):
        if f_player.get_rect().colliderect(ball.get_rect()):

            ball.speed_x = randint(5, 15)
            ball.speed_y = randint(5, 15)

            ball.angle += randint(20, 100)

    @staticmethod
    def s_player_vs_ball(s_player, ball):
        if s_player.get_rect().colliderect(ball.get_rect()):

            ball.speed_x = randint(5, 15)
            ball.speed_y = randint(5, 15)
            LoopFunctions.check_audio(Sounds.bat_ball_hit.play)

            ball.angle += randint(20, 100)

    @staticmethod
    def check_collisions(f_player, s_player, ball):
        Collisions.f_player_vs_ball(f_player, ball)
        Collisions.s_player_vs_ball(s_player, ball)

    @staticmethod
    def score_plus_plus(ball):
        if ball.x <= 270:
            Settings.s_player_score += 1
            ball.respawn()

            pygame.display.update()
            pygame.time.wait(300)

        if ball.x >= 1585:
            Settings.f_player_score += 1
            ball.respawn()

            pygame.display.update()
            pygame.time.wait(300)

    @staticmethod
    def check_score(restart_map):
        if Settings.f_player_score == 5:
            Settings.win_coins += 1
            Settings.score_coins += 5
            LoopFunctions.check_audio(Sounds.win.play)
            DataProcessing.save_data(str(Settings.win_coins), Settings.FILE_PATHS[1]["FILE"])
            DataProcessing.save_data(str(Settings.score_coins), Settings.FILE_PATHS[2]["FILE"])

            DrawUI.draw_text("I. PLAYER WON!", LoadingImages.BIG_FONT, "gold", 700, 600, LoadingImages.GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(1000)

            LoopFunctions.check_new_game()
            restart_map()

        if Settings.s_player_score == 5:
            LoopFunctions.check_audio(Sounds.win.play)
            DrawUI.draw_text("II. PLAYER WON!", LoadingImages.BIG_FONT, "gold", 700, 600, LoadingImages.GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(1000)

            LoopFunctions.check_new_game()
            restart_map()
