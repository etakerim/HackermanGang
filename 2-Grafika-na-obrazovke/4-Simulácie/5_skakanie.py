# https://www.youtube.com/watch?v=bz1gcTDxRPA
from pygame import *

WIDTH = 1000
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])
timer = time.Clock()

background = image.load("images/background.png").convert()
player_img = image.load("images/lamb.png").convert_alpha()
obstacle_img = image.load("images/hedgehog.png").convert_alpha()

GRAVITY = 4
JUMP_FORCE = -60

player_h = 150
player_x = 50
player_y = HEIGHT - player_h
player_vy = 0
player_img = transform.scale(player_img, [int(1.33*player_h), player_h])
background = transform.scale(background, [WIDTH, HEIGHT])

while True:
    event.poll()
    k = key.get_pressed()
    if player_y == HEIGHT - player_h and k[K_SPACE] == True:
        player_vy += JUMP_FORCE

    player_vy += GRAVITY
    player_y += player_vy

    if player_y < 0:
        player_y = 0
    elif player_y > HEIGHT - player_h:
        player_y = HEIGHT - player_h

    #screen.blit(background, [0, 0])
    screen.fill(Color(0,0,0))
    screen.blit(player_img, [player_x, player_y])
    display.update()
    timer.tick(20)