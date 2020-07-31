from pygame import *
from random import *

# 1. Mozaika
# 2. Redukovanie farebnej palety z 24-bitov na 8-bitov
# 3. Monochromatický obrázok
# 4. Poskladanie obrázkov vedľa seba (porovnanie)

WIDTH = 600
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])
parrot = image.load("parrot.jpg")
parrot = transform.scale(parrot, [WIDTH, HEIGHT])
res = 80
colors = 8

yblock = HEIGHT // res
xblock = WIDTH // res

for x in range(0, WIDTH, xblock):
    for y in range(0, HEIGHT, yblock):
        color = parrot.get_at([x, y])
        # Remove red from image: color.r = 0
        """
        color.r = int((color.r / 255) * colors) * (255 // colors)
        color.g = int((color.g / 255) * colors) * (255 // colors)
        color.b = int((color.b / 255) * colors) * (255 // colors)
        """
        c = int((color.g / 255) * colors) * (255 // colors)
        color = Color(c, c, c)

        draw.rect(screen, color, Rect(x, y, xblock, yblock))

while True:
    display.update()
    time.delay(30)