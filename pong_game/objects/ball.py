import pygame

from pong_game.sounds.sounds import Sounds
from pong_game.ui.loading_images import LoadingImages


class Ball:

    def __init__(self):
        self.image = LoadingImages.PONG_BALL[2]["BALL"]
        self.x = LoadingImages.GAME_SCREEN.get_width() / 2
        self.y = LoadingImages.GAME_SCREEN.get_height() / 2
        # self.speed = 10
        self.speed_x = 10
        self.speed_y = 10
        self.angle = 270

    @staticmethod
    def image_position(game_window, image, left_corner, angle):
        angle_position = pygame.transform.rotate(image, angle)

        hitbox = angle_position.get_rect(center=image.get_rect(topleft=left_corner).center)

        game_window.blit(angle_position, hitbox.topleft)

    def render_position(self, game_window):
        self.image_position(game_window, self.image, (self.x, self.y), self.angle)

    def movement(self):
        self.x += self.speed_x
        self.y += self.speed_y / 2

    def respawn(self):
        self.x = 900
        self.y = 540

    def ball_pos(self):
        if self.y >= 800:
            self.y -= 50

        if self.y <= 500:
            self.y -= 50

    def get_rect(self):
        rect_angle = pygame.transform.rotate(self.image, self.angle)
        rect = rect_angle.get_rect(topleft=(self.x, self.y), center=(
            self.x + (self.image.get_width() / 2), self.y + (self.image.get_height() / 2)))

        return rect

    def out_of_screen(self):
        if self.y <= 0 or self.y >= 1920:
            # self.y *= -1
            self.y = 500
        if self.x <= 0 or self.x >= 1080:
            # self.x *= -1
            self.x = 500

        # if self.x

    def screen_edge(self):
        if self.y >= LoadingImages.GAME_SCREEN.get_height() or self.y <= 0:
            self.speed_y *= -1
            # ball.y += ball.speed_y
            Sounds.ball_hit.play()

        if self.x >= LoadingImages.GAME_SCREEN.get_width() or self.x <= 0:
            self.speed_x *= -1
            # ball.x += ball.speed_x
            Sounds.ball_hit.play()

    def table_edge(self):
        if self.y <= 200 or self.y >= 880:
            if self.x >= 570 or self.x <= 1280:
                self.speed_y *= -1
                # ball.y += ball.speed_y
                Sounds.ball_hit.play()

        #if self.x >= LoadingImages.GAME_SCREEN.get_width() or self.x <= 0:
            #self.speed_x *= -1
            # ball.x += ball.speed_x
            #Sounds.ball_hit.play()