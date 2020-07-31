from pygame import *

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

WIDTH = 600
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])

screen.fill(WHITE)
draw.line(screen, BLACK, [0, HEIGHT // 3], [WIDTH, HEIGHT // 3], 5)
draw.line(screen, BLACK, [0, HEIGHT // 3 * 2], [WIDTH, HEIGHT // 3 * 2], 5)

draw.line(screen, BLACK, [WIDTH // 3, 0], [WIDTH // 3, HEIGHT], 5)
draw.line(screen, BLACK, [WIDTH // 3 * 2, 0], [WIDTH // 3 * 2, HEIGHT], 5)

display.update()