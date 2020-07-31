from pygame import *

ZELENA = Color(0, 255, 0)
BIELA = Color(255, 255, 255)
RED = Color(255, 0, 0)
ROZLISENIE = [1000, 1000]
okno = display.set_mode(ROZLISENIE)

"""
x = []
for i in range(0, 5):
    x.append(0)
"""

x = [0, 0, 0, 0, 0]
y = [10, 40, 150, 500, 200]
vx = [5, 10, 8, 5, 5]
vy = [5, 10, 8, 5, 5]
mysx = 0
mysy = 0


while True:
    udalost = event.poll()
    if udalost.type == MOUSEMOTION:
        mysx = udalost.pos[0]
        mysy = udalost.pos[1]

    okno.fill(BIELA)
    draw.rect(okno, ZELENA, Rect([mysx, mysy], [100, 100]))

    for i in range(len(x)):
        x[i] = x[i] + vx[i]
        y[i] = y[i] + vy[i]

        if x[i] < 0:
           vx[i] = -vx[i]
        if x[i] > 1000:
           vx[i] = -vx[i]

        if y[i] < 0:
           vy[i] = -vy[i]
        if y[i] > 1000:
           vy[i] = -vy[i]


        if x[i] + 100 < mysx or mysx + 100 < x[i] or y[i] + 100 < mysy or mysy + 100 < y[i]:
            draw.rect(okno, ZELENA, Rect([x[i], y[i]], [100, 100]))
        else:
            draw.rect(okno, RED, Rect([x[i], y[i]], [100, 100]))

    display.update()
    time.delay(20)