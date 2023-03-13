import math

import pygame


class Player:
    FULL_DEGREES = 360
    HALF_DEGREES = 180

    PI = 3.14

    def __init__(self):
        self.image = self.image
        self.x = self.x_position
        self.y = self.y_position
        self.speed = 2
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

    def movement(self):
        plane_angle = self.angle * (self.PI / self.HALF_DEGREES)

        self.x += -self.speed * math.sin(plane_angle)
        self.y += -self.speed * math.cos(plane_angle)

    def up(self):
        #self.speed = min(self.speed + self.speed, self.max_speed)

        #self.movement()

        self.y -= 10

    def down(self):
        #self.speed = max(self.speed - self.speed, -6)

        #self.movement()

        self.y += 10

    def right(self):
        #self.speed = max(self.speed - self.speed, -6)

        #self.movement()

        self.x += 10

    def left(self):
        #self.speed = min(self.speed + self.speed, self.max_speed)

        #self.movement()

        self.x -= 10
