import pygame
import sys
import random

ROZLISENIE = (640, 480)
FARBA_BCG = (0xc9, 0xd6, 0xdd)

pygame.init()
platno = pygame.display.set_mode(ROZLISENIE)
pygame.display.set_caption("Grafický program")

while True:
    platno.fill(FARBA_BCG)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    for polomer in range(5, 150, 10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.circle(platno, (r, g, b), (300, 300), polomer, 5)
        
        
    pygame.display.update()
