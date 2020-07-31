from pygame import *
from math import *

WIDTH = 1000
HEIGHT = 1000

WHITE = Color(255, 255, 255)
screen = display.set_mode([WIDTH, HEIGHT])

def hexagon(x, y, r):
    points = []
    v = Vector2(r, 0)
    v = v.rotate(30)

    for i in range(6):
        points.append([x + int(v.x), y + int(v.y)])
        v = v.rotate(60)
    return points

def comb(x, y, r, layer):
    layer += 1
    if layer > 5:
        return

    draw.polygon(screen, WHITE, hexagon(x, y, r), 1)
    display.update()
    time.delay(30)

    v = Vector2(layer * sqrt(3) * r, 0)

    for i in range(6):
        comb(x + int(v.x), y + int(v.y), r, layer)
        v = v.rotate(60)

comb(WIDTH // 2, HEIGHT // 2, 20, 0)
display.update()