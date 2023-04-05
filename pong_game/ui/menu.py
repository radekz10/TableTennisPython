import pygame

from pong_game.config.settings import Settings
from pong_game.loop.matches import Match
from pong_game.ui.button import Button
from pong_game.ui.draw_ui import DrawUI
from pong_game.ui.loading_images import LoadingImages


class Menu:
    TITLE_Y = 70
    TITLE_COLOR = "orange"
    QUIT_X = 977
    QUIT_Y = 980

    # MAIN MENU --------------------------------------------------------------------------------------------------------
    @staticmethod
    def main_menu():

        while 1:

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("MAIN MENU", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 750, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            play_button = Button(button_image=LoadingImages.BUTTONS[2]["BUTTON"], x_y=(976, 430),
                                 button_text="PLAY",
                                 font=LoadingImages.BIG_FONT,
                                 font_color="white", font_hover_color="cyan")

            stats_button = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(977, 580),
                                  button_text="STATS",
                                  font=LoadingImages.NORMAL_FONT,
                                  font_color="white", font_hover_color="cyan")

            binds_button = Button(button_image=LoadingImages.BUTTONS[6]["BUTTON"], x_y=(60, 60), button_text="",
                                  font=LoadingImages.NORMAL_FONT,
                                  font_color="white", font_hover_color="cyan")

            settings_button = Button(button_image=LoadingImages.BUTTONS[5]["BUTTON"], x_y=(1860, 60), button_text="",
                                     font=LoadingImages.NORMAL_FONT,
                                     font_color="white", font_hover_color="cyan")

            quit_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="QUIT",
                                 font=LoadingImages.NORMAL_FONT,
                                 font_color="orange", font_hover_color="red")

            play_button.button_render(LoadingImages.GAME_SCREEN)

            stats_button.button_render(LoadingImages.GAME_SCREEN)
            binds_button.button_render(LoadingImages.GAME_SCREEN)
            settings_button.button_render(LoadingImages.GAME_SCREEN)
            quit_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(play_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(stats_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(binds_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(settings_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(quit_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.on_click(mouse_coordinates):
                        Match.f_match()
                    if stats_button.on_click(mouse_coordinates):
                        Menu.stats()
                    if binds_button.on_click(mouse_coordinates):
                        Menu.binds()
                    if settings_button.on_click(mouse_coordinates):
                        Menu.game_settings()
                    if quit_button.on_click(mouse_coordinates):
                        pygame.quit()

            pygame.display.update()

    @staticmethod
    def stats():

        global pointer_left_button, pointer_right_button

        loading = 1

        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))

            while loading:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[3]["BACKGROUND"], (0, 0))
                DrawUI.draw_text("Loading Stats.", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)

                DrawUI.draw_text("Loading Stats..", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)

                DrawUI.draw_text("Loading Stats...", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)
                loading = False

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("STATS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 840, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("WINS", LoadingImages.MEDIUM_FONT, "purple", 680, 330,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (750, 410))
            DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.BIG_FONT, "white", 630, 400,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.star_icon, (1250, 405))
            DrawUI.draw_text("SCORE", LoadingImages.MEDIUM_FONT, "purple", 1180, 330,
                             LoadingImages.GAME_SCREEN)

            # LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (750, 400))
            DrawUI.draw_text(f"{Settings.score_coins}", LoadingImages.BIG_FONT, "white", 1130, 400,
                             LoadingImages.GAME_SCREEN)

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()

    # GAME BINDS ---------------------------------------------------------------------------------------------------

    @staticmethod
    def binds():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("BINDS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 850, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("CONTROL", LoadingImages.NORMAL_FONT, "purple", 540, 200, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("W", LoadingImages.MEDIUM_FONT, "white", 595, 280, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("I", LoadingImages.MEDIUM_FONT, "white", 663, 280, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Forward", LoadingImages.MEDIUM_FONT, "cyan", 1220, 280, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("S", LoadingImages.MEDIUM_FONT, "white", 600, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("K", LoadingImages.MEDIUM_FONT, "white", 660, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Backward", LoadingImages.MEDIUM_FONT, "cyan", 1220, 330, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("A", LoadingImages.MEDIUM_FONT, "white", 600, 380, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("J", LoadingImages.MEDIUM_FONT, "white", 660, 380, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Left", LoadingImages.MEDIUM_FONT, "cyan", 1220, 380, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("D", LoadingImages.MEDIUM_FONT, "white", 600, 430, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("L", LoadingImages.MEDIUM_FONT, "white", 660, 430, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Right", LoadingImages.MEDIUM_FONT, "cyan", 1220, 430, LoadingImages.GAME_SCREEN)

            #DrawUI.draw_text("CAR ABILITIES", LoadingImages.NORMAL_FONT, "purple", 495, 480, LoadingImages.GAME_SCREEN)

            # DrawUI.draw_text("E", LoadingImages.MEDIUM_FONT, "white", 632, 560, LoadingImages.GAME_SCREEN)
            # DrawUI.draw_text("Nitro", LoadingImages.MEDIUM_FONT, "cyan", 1220, 560, LoadingImages.GAME_SCREEN)

            # DrawUI.draw_text("Q", LoadingImages.MEDIUM_FONT, "white", 630, 610, LoadingImages.GAME_SCREEN)
            # DrawUI.draw_text("Faster Movement", LoadingImages.MEDIUM_FONT, "cyan", 1220, 610, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("IN-GAME", LoadingImages.NORMAL_FONT, "purple", 550, 660, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("R", LoadingImages.MEDIUM_FONT, "white", 630, 740, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Restart Game", LoadingImages.MEDIUM_FONT, "cyan", 1220, 740, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("X", LoadingImages.MEDIUM_FONT, "white", 630, 790, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Exit", LoadingImages.MEDIUM_FONT, "cyan", 1220, 790, LoadingImages.GAME_SCREEN)

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()

    # GAME SETTINGS ----------------------------------------------------------------------------------------------------
    @staticmethod
    def game_settings():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("SETTINGS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 790, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("AUDIO", LoadingImages.NORMAL_FONT, "cyan", 620, 300, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("VSYNC", LoadingImages.NORMAL_FONT, "cyan", 620, 400, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("UI", LoadingImages.NORMAL_FONT, "cyan", 620, 500, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("FPS", LoadingImages.NORMAL_FONT, "cyan", 620, 600, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("XY", LoadingImages.NORMAL_FONT, "cyan", 620, 700, LoadingImages.GAME_SCREEN)

            audio_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 340),
                                     button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                     font_hover_color="cyan")

            audio_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 340),
                                      button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                      font_hover_color="purple")

            vsync_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 440),
                                     button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                     font_hover_color="cyan")
            vsync_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 440),
                                      button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                      font_hover_color="purple")

            show_ui_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 540),
                                       button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                       font_hover_color="cyan")
            show_ui_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 540),
                                        button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="purple")

            show_fps_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 640),
                                        button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="cyan")
            show_fps_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 640),
                                         button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                         font_hover_color="purple")

            show_xy_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 740),
                                       button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                       font_hover_color="cyan")
            show_xy_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 740),
                                        button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="purple")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            audio_on_button.button_render(LoadingImages.GAME_SCREEN)
            audio_off_button.button_render(LoadingImages.GAME_SCREEN)

            vsync_on_button.button_render(LoadingImages.GAME_SCREEN)
            vsync_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_ui_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_ui_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_xy_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_xy_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_fps_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_fps_off_button.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(audio_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(audio_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(vsync_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(vsync_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_ui_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_ui_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_xy_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_xy_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_fps_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_fps_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    settings_options = {
                        audio_on_button: ("AUDIO ON!", 850, 210, 1),
                        audio_off_button: ("AUDIO OFF!", 850, 210, 2),
                        vsync_on_button: ("VSYNC ON!", 850, 210, 1),
                        vsync_off_button: ("VSYNC OFF!", 850, 210, 0),
                        show_ui_on_button: ("UI ON!", 900, 210, 1),
                        show_ui_off_button: ("UI OFF!", 900, 210, 2),
                        show_fps_on_button: ("FPS ON!", 890, 210, 1),
                        show_fps_off_button: ("FPS OFF!", 890, 210, 2),
                        show_xy_on_button: ("X-Y ON!", 890, 210, 1),
                        show_xy_off_button: ("X-Y OFF!", 890, 210, 2),
                    }

                    for button, (text, x, y, value) in settings_options.items():

                        if button.on_click(mouse_coordinates):
                            if button in (audio_on_button, audio_off_button):
                                Settings.audio = value
                            elif button in (vsync_on_button, vsync_off_button):
                                Settings.vsync = value
                                print(Settings.vsync)
                            elif button in (show_ui_on_button, show_ui_off_button):
                                Settings.show_ui = value
                            elif button in (show_fps_on_button, show_fps_off_button):
                                Settings.show_fps = value
                            elif button in (show_xy_on_button, show_xy_off_button):
                                Settings.show_xy = value

                            DrawUI.draw_text(text, LoadingImages.NORMAL_FONT, "green", x, y, LoadingImages.GAME_SCREEN)
                            pygame.display.update()
                            pygame.time.wait(1200)

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()
