import pygame
from pygame.locals import *
import sys

BIELA = (255, 255, 255)
MODRA = (0, 0, 255)

pygame.init()
okno = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Graph paper")
okno.fill(BIELA)
pygame.draw.circle(okno, MODRA, (100, 100), 50, 0)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

