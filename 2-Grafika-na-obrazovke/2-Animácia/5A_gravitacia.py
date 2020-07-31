from pygame import *
from math import hypot
from random import *

CERVENA = Color(255, 0, 0)
ROZLISENIE = [1000, 800]
okno = display.set_mode(ROZLISENIE)

x = randint(0, 1000)
y = randint(0, 800)
vx = 0
vy = 0
ax = 0
ay = 0
mysX = 0
mysY = 0

while True:
    mys = event.poll()
    if mys.type == MOUSEMOTION:
        mysX = mys.pos[0]
        mysY = mys.pos[1]

    ax = mysX - x
    ay = mysY - y
    length = hypot(ax, ay)
    ax = 0.5 * (ax / length)
    ay = 0.5 * (ay / length)

    vx = vx + ax
    vy = vy + ay

    x = x + vx
    y = y + vy

    draw.circle(okno, CERVENA, [int(x), int(y)], 2)
    display.update()
    time.delay(10)