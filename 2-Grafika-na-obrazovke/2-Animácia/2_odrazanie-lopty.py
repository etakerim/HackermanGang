from pygame import *

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
WIDTH = 600
HEIGHT = 400

r = 20

x = r
y = r
vx = 5
vy = 8

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    # Zmeň polohu podľa rýchlosti
    x += vx
    y += vy

    # Uprav vektor rýchlosti
    if x - r < 0 or x + r > WIDTH:
        vx = -vx
    if y - r < 0 or y + r > HEIGHT:
        vy = -vy

    # Nakresli
    screen.fill(BLACK)
    draw.circle(screen, RED, (x, y), r)
    display.update()
    time.delay(16)