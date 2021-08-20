import pygame
import random
class Enemy:
    ENEMY_PNG = pygame.image.load('images/alien.png')
    YVEL = 3
    last_spwan = 0
    SPAWN_RATE = 1.5

    def __init__(self, y, screen):
        self.x = random.randint(64, screen.get_width() - 64)
        self.y = y
        self.INITIAL_Y = y
        self.screen = screen

    def move(self, dt):
        self.y += self.YVEL * dt
        self.screen.blit(self.ENEMY_PNG, (self.x, self.y))