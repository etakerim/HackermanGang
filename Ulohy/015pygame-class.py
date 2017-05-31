import sys
import pygame

VELKOST_OKNA = (640, 480)
FARBA_BCG = ((0xc9, 0xd6, 0xdd))

pygame.init()
platno = pygame.display.set_mode(VELKOST_OKNA)
pygame.display.set_caption("Prvy graficky program")


while True:
    pygame.display.update()
    platno.fill(FARBA_BCG)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            mousex, mousey = ev.pos
        elif ev.type == pygame.MOUSEMOTION:
            mousex, mousey = ev.pos
        print(mousex, mousey)

