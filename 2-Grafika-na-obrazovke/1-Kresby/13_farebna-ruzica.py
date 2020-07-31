import pygame
from random import randrange

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))

while True:
    v = pygame.Vector2()
    angle = randrange(360)
    v.from_polar((100, angle))

    color = pygame.Color(0, 0, 0)
    color.hsva = (angle, 100, 100)

    pygame.draw.line(screen, color, (300, 300), (300 + int(v.x), 300 + int(v.y)))
    pygame.display.update()
    pygame.time.delay(16)

pygame.display.update()