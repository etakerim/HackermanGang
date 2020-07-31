from opensimplex import *
from pygame import *

WIDTH = 600
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])
generator = OpenSimplex()
f = 3

for y in range(HEIGHT):
    for x in range(WIDTH):
        nx = x / WIDTH
        ny = y / HEIGHT
        # h = generator.noise2d(f * nx, f * ny)
        # c = int((h + 1) * 120)
        # color = Color(c, c, c)

        h = (generator.noise2d(f*nx, f*ny) +
            0.5 * generator.noise2d(4*f*nx, 4*f*ny) +
            0.25 * generator.noise2d(8*f*nx, 8*f*ny) +
            0.125 * generator.noise2d(16*f*nx, 16*f*ny))

        if h < -0.2:
            color = Color(50, 80, 160)      # Hlboké more
        elif h < 0:
            color = Color(50, 100, 200)     # Morská plytčina
        elif h < 0.07:
            color = Color(221, 197, 111)    # Pláž
        elif h < 0.5:
            color = Color(70, 160, 70)      # Pláne
        elif h < 0.6:
            color = Color(90, 90, 80)       # Okraje hôr
        elif h < 0.8:
            color = Color(110, 110, 95)     # Hory
        else:
            color = Color(140, 130, 120)    # Kamenné vrcholce hôr

        screen.set_at([x, y], color)

while True:
    display.update()
    time.delay(20)