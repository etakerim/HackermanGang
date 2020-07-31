from pygame import *

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

WIDTH = 600
HEIGHT = 600
screen = display.set_mode((WIDTH, HEIGHT))

policka = 8
riadok = HEIGHT // policka
stlpec = WIDTH // policka

color = WHITE

for r in range(policka):
    for s in range(policka):
        y = r * riadok
        x = s * stlpec
        draw.rect(screen, color, (x, y, riadok, stlpec))
        if color == BLACK:
            color = WHITE
        else:
            color = BLACK
    if color == BLACK:
        color = WHITE
    else:
        color = BLACK

display.update()