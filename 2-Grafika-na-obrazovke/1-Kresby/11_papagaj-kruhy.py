from pygame import *
from random import *

WIDTH = 600
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])
parrot = image.load("parrot.jpg")
parrot = transform.scale(parrot, [WIDTH, HEIGHT])
r = 5

while True:
    x = randrange(WIDTH)
    y = randrange(HEIGHT)
    color = parrot.get_at([x, y])
    draw.circle(screen, color, [x, y], r)
    display.update()
    time.delay(30)