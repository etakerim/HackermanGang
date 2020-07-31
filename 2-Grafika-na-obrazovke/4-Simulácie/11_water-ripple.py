import pygame
from pygame import PixelArray

WIDTH = 200
HEIGHT = 200

damping = 0.8

curr = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
prev = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        curr[mouse[0]][mouse[1]] = 255

    water = PixelArray(screen)
    for x in range(1, WIDTH - 1):
        for y in range(1, HEIGHT - 1):
            curr[x][y] = (prev[x-1][y] + prev[x+1][y] + prev[x][y+1] + prev[x][y-1]) / 2 - curr[x][y]
            curr[x][y] *= damping
            c = curr[x][y] * 255
            if c < 0:
                c = 0
            elif c > 255:
                c = 255
            water[x, y] = (c, c, c)
    water.close()
    prev, curr = curr, prev
    pygame.display.update()
