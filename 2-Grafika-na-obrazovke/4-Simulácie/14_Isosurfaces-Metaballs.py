from pygame import *
from random import *

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

WIDTH = 500
HEIGHT = 500
r = 40
screen = display.set_mode([WIDTH, HEIGHT])

blob = Vector2(100, 100)
velocity = Vector2()
velocity.from_polar((uniform(20, 25), randrange(360)))

while True:
    screen.fill(BLACK)

    pixels = PixelArray(screen)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos = Vector2(x, y)
            middle = Vector2(blob.x, blob.y)
            d = pos.distance_to(middle)
            c = 0
            if d == 0:
                c = 255
            else:
                c = min(int(300 * r / d), 255)
            pixels[x, y] = Color(c, c, c)

    pixels.close()
    # draw.circle(screen, WHITE, [int(blob.x), int(blob.y)], r)
    blob += velocity

    display.update()