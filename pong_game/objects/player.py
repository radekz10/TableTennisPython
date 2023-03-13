import pygame


class Player:

    def __init__(self):
        self.image = self.image
        self.x = self.x_position
        self.y = self.y_position
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
