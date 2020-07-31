import sys
import pygame


pygame.init()
size = [800, 480]
canvas = pygame.display.set_mode(size)

r = 5
canvas.fill((0, 0, 0))

def half_rombus(x_inc):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    a = [size[0] // 2, 20]
    b = [size[0] // 2, size[1] - 20]

    for n in reversed(range(1, 7)):
        pygame.draw.line(canvas, WHITE, a, b)
        dy = (b[1] - a[1]) // n
        for y in range(a[1], b[1] + 1, dy):
            pygame.draw.ellipse(canvas, BLUE, (a[0] - r, y - r, 2*r, 2*r))
        a = [a[0] + x_inc, a[1] + dy // 2]
        b = [b[0] + x_inc, b[1] - dy // 2]

half_rombus(50)
half_rombus(-50)
pygame.display.update()

while True:
    pygame.time.delay(30)
