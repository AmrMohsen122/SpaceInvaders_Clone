import math
import pygame


class SpaceShip:
    SPACESHIP_PNG = pygame.image.load('images/space-invaders.png')
    PLAYER_XVEL = 5.25
    PLAYER_YVEL = 5.25

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def move(self, dir, dt):
        if dir == "UP":
            self.y -= self.PLAYER_YVEL * dt
        elif dir == "DOWN":
            self.y += self.PLAYER_YVEL * dt
        elif dir == "LEFT":
            self.x -= self.PLAYER_XVEL * dt
        elif dir == "RIGHT":
            self.x += self.PLAYER_XVEL * dt

    def draw(self):
        self.screen.blit(self.SPACESHIP_PNG, (self.x, self.y))

    def hasCollided(self, objects):
        for object in objects:
            distance = math.sqrt((self.x - object.x) * (self.x - object.x) + (self.y - object.y) * (self.y - object.y))
            if distance <= 62:
                return True
        return False


class Bullet:
    BULLET_PNG = pygame.image.load("images/bullet.png")
    YVEL = 4.5
    BULLETS_FIRING_SPEED = 0.25
    prev_shot_time = 0

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def fire(self):
        self.screen.blit(self.BULLET_PNG, (self.x, self.y))

    def move(self, dt):
        self.y -= self.YVEL * dt
        self.screen.blit(self.BULLET_PNG, (self.x, self.y))

    def hasCollided(self, objects):
        i = 0
        for object in objects:
            distance = math.sqrt((self.x - object.x) * (self.x - object.x) + (self.y - object.y) * (self.y - object.y))
            if distance <= 45:
                return True, i
            i += 1
        return False, -1
