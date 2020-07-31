from pygame import *

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
WIDTH = 600
HEIGHT = 400

R = 20
x = R
vx = 15

screen = display.set_mode([WIDTH, HEIGHT])
area = screen.get_rect()

while True:
    x += vx
    if x - R <= 0 or x + R >= WIDTH:
        vx *= -1

    screen.fill(BLACK, area)
    prev = area
    area = draw.circle(screen, RED, [x, HEIGHT // 2], R)
    display.update([prev, area])
    time.delay(30)