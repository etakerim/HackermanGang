from pygame import *
from random import *

WIDTH = 400
HEIGHT = 400

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
x = 200
y = 200

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    smer = randrange(4)
    if smer == 0:
        x = x + 1
    elif smer == 1:
        x = x - 1
    elif smer == 2:
        y = y + 1
    elif smer == 3:
        y = y - 1

    screen.set_at([x, y], WHITE)
    display.update()
    time.delay(16)