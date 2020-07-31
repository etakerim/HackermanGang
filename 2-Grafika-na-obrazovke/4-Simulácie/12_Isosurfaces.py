from pygame import *

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

WIDTH = 500
HEIGHT = 500

screen = display.set_mode([WIDTH, HEIGHT])

pixels = PixelArray(screen)
for y in range(HEIGHT):
    for x in range(WIDTH):
        # Kruhový gradient
        """pos = Vector2(x, y)
        middle = Vector2(WIDTH / 2, HEIGHT / 2)
        c = min(int(pos.distance_to(middle)), 255)
        pixels[x, y] = Color(c, c, c)
        """
        # Lineárny gradient
        """c = int(255 * (x / WIDTH))
        pixels[x, y] = Color(c, c, c)
        """

        # RGB farby
        cx = int(255 * (x / WIDTH))
        cy = int(255 * (y / HEIGHT))
        pixels[x, y] = Color(cx, 0, cy)
        # pixels[x, y] = Color(x % 255, 0, y % 255)

pixels.close()

display.update()