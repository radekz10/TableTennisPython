import pygame

from pong_game.ui.loading_images import LoadingImages


class Ball:

    def __init__(self):
        self.image = LoadingImages.PONG_BALL[1]["BALL"]
        self.x = 900
        self.y = 540
        self.speed = 10
        self.angle = 270

    @staticmethod
    def image_position(game_window, image, left_corner, angle):
        angle_position = pygame.transform.rotate(image, angle)

        hitbox = angle_position.get_rect(center=image.get_rect(topleft=left_corner).center)

        game_window.blit(angle_position, hitbox.topleft)

    def render_position(self, game_window):
        self.image_position(game_window, self.image, (self.x, self.y), self.angle)

    def collision(self):
        self.speed += 10
        self.x += 50

    def collisionn(self):
        self.speed -= 10
        self.x -= 50

    def get_rect(self):
        rect_angle = pygame.transform.rotate(self.image, self.angle)
        rect = rect_angle.get_rect(topleft=(self.x, self.y),
                                   center=(self.x + (self.image.get_width() / 2), self.y + (self.image.get_height() / 2)))

        return rect
