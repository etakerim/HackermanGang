from pygame import *
from random import *

WIDTH = 600
HEIGHT = 400
screen = display.set_mode([WIDTH, HEIGHT])

for y in range(HEIGHT):
    for x in range(WIDTH):
        c = randrange(256)
        screen.set_at([x, y], Color(c, c, c))

while True:
    display.update()
    time.delay(30)