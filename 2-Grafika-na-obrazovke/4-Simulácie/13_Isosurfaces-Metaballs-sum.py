from pygame import *
from random import *

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

WIDTH = 500
HEIGHT = 500
r = 40

blobs = []
for i in range(5):
    velocity = Vector2()
    velocity.from_polar((uniform(20, 25), randrange(360)))
    b = {
        "pos": Vector2(randrange(WIDTH), randrange(HEIGHT)),
        "vel": velocity,
    }
    blobs.append(b)


screen = display.set_mode([WIDTH, HEIGHT])
while True:
    screen.fill(BLACK)

    pixels = PixelArray(screen)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            suma = 0
            for blob in blobs:
                pos = Vector2(x, y)
                middle = Vector2(blob["pos"].x, blob["pos"].y)
                d = pos.distance_to(middle)
                if d == 0:
                    suma += 255
                else:
                    suma += int(200 * r / d)
            suma = min(suma, 255)
            pixels[x, y] = Color(suma, suma, suma)

    pixels.close()
    for blob in blobs:
        blob["pos"] += blob["vel"]
        if blob["pos"].x < 0 or blob["pos"].x > WIDTH:
            blob["vel"].x = -blob["vel"].x
        if blob["pos"].y < 0 or blob["pos"].y > HEIGHT:
            blob["vel"].y = -blob["vel"].y

    display.update()