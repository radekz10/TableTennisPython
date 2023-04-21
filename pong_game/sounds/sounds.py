import pygame

# pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Sounds:
    ball_hit = pygame.mixer.Sound("../sound_effects/ball_hit.mp3")
    ball_hit.set_volume(0.1)

    bat_ball_hit = pygame.mixer.Sound("../sound_effects/bat_ball_hit.ogg")
    bat_ball_hit.set_volume(0.1)

    # GAME EVENT SOUNDS -----------------------------------------------------------------------------------------------

    countdown = pygame.mixer.Sound("../sound_effects/countdown.wav")
    countdown.set_volume(0.1)

    finish = pygame.mixer.Sound("../sound_effects/finish.wav")
    finish.set_volume(0.1)

    win = pygame.mixer.Sound("../sound_effects/win.wav")
    win.set_volume(0.1)

    lose = pygame.mixer.Sound("../sound_effects/lose.wav")
    lose.set_volume(0.1)
