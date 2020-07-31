from pygame import *
from random import *

# Úlohy obdĺžky, kruhy vedľa seba, v sebe, s posunom
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
PINK = Color(168, 50, 166)

WIDTH = 600
HEIGHT = 400

screen = display.set_mode([WIDTH, HEIGHT])
circles = []
r = 20

screen.fill(WHITE)

while len(circles) < 100:
    circle = Vector2(randrange(WIDTH), randrange(WIDTH))

    overlaping = False
    for c in circles:
        if circle.distance_to(c) < 2*r:
            overlaping = True
            break
    if not overlaping:
        circles.append(circle)

for circle in circles:
    draw.circle(screen, PINK, [int(circle.x), int(circle.y)], r)
display.update()
time.delay(16)