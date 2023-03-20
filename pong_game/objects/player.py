import math

import pygame


class Player:

    def __init__(self):
        self.image = self.image
        self.x = self.x_position
        self.y = self.y_position
        self.speed = 10
        self.max_speed = 3
        self.movement_speed = 2
        self.max_movement_speed = 5
        self.angle = self.angle

    @staticmethod
    def image_position(game_window, image, left_corner, angle):
        angle_position = pygame.transform.rotate(image, angle)

        hitbox = angle_position.get_rect(center=image.get_rect(topleft=left_corner).center)

        game_window.blit(angle_position, hitbox.topleft)

    def render_position(self, game_window):
        self.image_position(game_window, self.image, (self.x, self.y), self.angle)

    def get_rect(self):
        rect_angle = pygame.transform.rotate(self.image, self.angle)
        rect = rect_angle.get_rect(topleft=(self.x, self.y),
                                   center=(self.x + (self.image.get_width() / 2), self.y + (self.image.get_height() / 2)))

        return rect

    def up(self):
        self.y -= self.speed

    def down(self):
        self.y += self.speed

    def right(self):
        self.x += self.speed

    def left(self):
        self.x -= self.speed

    def rotate_left(self):
        self.angle -= self.angle

    def rotate_right(self):
        self.angle += self.angle
