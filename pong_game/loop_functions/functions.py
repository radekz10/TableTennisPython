import pygame

from pong_game.config.settings import Settings
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class LoopFunctions:

    @staticmethod
    def check_new_game():
        Settings.started = False

        while not Settings.started:
            # LoadingImages.GAME_SCREEN.blit(LoadingImages.TIME_TABLES[1]["TABLE"], (700, 200))
            DrawUI.draw_text("PLAY AGAIN - SPACE", LoadingImages.NORMAL_FONT, "white", 740, 250,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("EXIT TO MENU - X", LoadingImages.NORMAL_FONT, "cyan", 740, 350, LoadingImages.GAME_SCREEN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Settings.started = 1
                    Settings.car_start_time = pygame.time.get_ticks()

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

                    Settings.car_start_time = pygame.time.get_ticks()
                    Settings.enemy_start_time = pygame.time.get_ticks()

    @staticmethod
    def start_countdown(f_player, s_player):
        if Settings.countdown > 0:

            count_timer = pygame.time.get_ticks()
            f_player.max_speed = 0

            s_player.max_speed = 0

            if count_timer - Settings.last_count > 1000:
                Settings.countdown -= 1
                Settings.last_count = count_timer

        if Settings.countdown == 5:
            DrawUI.draw_text(f"{str(Settings.countdown)} - 5", LoadingImages.NORMAL_FONT, "red", 850, 570,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 4:
            DrawUI.draw_text(f"{str(Settings.countdown)} - 4", LoadingImages.NORMAL_FONT, "red", 850, 570,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 3:
            DrawUI.draw_text(f"{str(Settings.countdown)} - 3", LoadingImages.NORMAL_FONT, "red", 850, 570,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 2:
            DrawUI.draw_text(f"{str(Settings.countdown)} - 2", LoadingImages.NORMAL_FONT, "red", 850, 570,
                             LoadingImages.GAME_SCREEN)

        if Settings.countdown == 1:
            DrawUI.draw_text(f"{str(Settings.countdown)} - 1", LoadingImages.NORMAL_FONT, "red", 850, 570,
                             LoadingImages.GAME_SCREEN)
