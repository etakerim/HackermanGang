from pygame import *
from random import *

WIDTH = 400
HEIGHT = 400

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
pos = Vector2(200, 200)
prev = Vector2(pos)

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    step = Vector2()
    # Ver.1: step.from_polar((5, randrange(360)))
    # Ver.2:
    step.from_polar((2, randrange(360)))
    if random() < 0.01:
        step.scale_to_length(randint(25, 100))

    prev.update(pos)
    pos = pos + step

    draw.line(screen, WHITE, [prev.x, prev.y], [pos.x, pos.y])
    display.update()
    time.delay(16)