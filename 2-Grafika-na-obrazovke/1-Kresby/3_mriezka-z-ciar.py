from pygame import *

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

screen = display.set_mode([600, 600])

screen.fill(WHITE)
draw.line(screen, BLACK, [0, 200], [600, 200], 5)
draw.line(screen, BLACK, [0, 400], [600, 400], 5)

draw.line(screen, BLACK, [200, 0], [200, 600], 5)
draw.line(screen, BLACK, [400, 0], [400, 600], 5)

display.update()