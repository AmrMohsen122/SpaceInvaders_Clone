import pygame
import random
import math
import time
from pygame import mixer
from player import SpaceShip, Bullet
from enemy import Enemy

pygame.init()
running = True

# WINDOW
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
logo = pygame.image.load('images/ufo.png').convert()
pygame.display.set_icon(logo)
background_png = pygame.image.load('images/background.png')

# PLAYER
player = SpaceShip(360, 480, screen)
# ENEMY
enemy_y = 10
enemies = []
# BULLET
bullets = []
# MUSIC
mixer.music.load('audio/background.wav')
mixer.music.play(-1)
COLLISION_SOUND = mixer.Sound("audio/explosion.wav")
SHOOTING_SOUND = mixer.Sound("audio/laser.wav")
# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameover_font = pygame.font.Font('freesansbold.ttf', 42)

textX = 10
textY = 10
# framerate independance
last_time = time.time()
while running:
    dt = (time.time() - last_time) * 60
    last_time = time.time()
    screen.blit(background_png, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.x >= 0:
            player.move("LEFT", dt)
    if keys[pygame.K_RIGHT]:
        if player.x <= screen_width - 64:
            player.move("RIGHT", dt)
    if keys[pygame.K_UP]:
        if player.y >= 0:
            player.move("UP", dt)
    if keys[pygame.K_DOWN]:
        if player.y <= screen_height - 64:
            player.move("DOWN", dt)
    if keys[pygame.K_SPACE] and time.time() - Bullet.prev_shot_time >= Bullet.BULLETS_FIRING_SPEED:
        Bullet.prev_shot_time = time.time()
        bullet = Bullet(player.x + 16, player.y + 32, screen)
        bullets.append(bullet)
        SHOOTING_SOUND.play()
        bullet.fire()
    # bullet movement
    i = 0
    while i < len(bullets):
        hasCollided = bullets[i].hasCollided(enemies)
        if hasCollided[0]:
            COLLISION_SOUND.play()
            del (bullets[i])
            del (enemies[hasCollided[1]])
            score += 1
            i -= 1
        else:
            bullets[i].move(dt)
        i += 1

    # spawning enemies
    if time.time() - Enemy.last_spwan >= Enemy.SPAWN_RATE:
        Enemy.last_spwan = time.time()
        enemies.append(Enemy(enemy_y, screen))
    # enemy movement
    for enemy in enemies:
        enemy.move(dt)
    if player.hasCollided(enemies):
        game_over = gameover_font.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over, (screen_width / 2 - 95, screen_height / 2 - 35))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (textX, textY))
    player.draw()
    pygame.display.update()
pygame.quit()
