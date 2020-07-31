from pygame import *
from math import *

BIELA = Color(255, 255, 255)
# R, G, B
ZELENA = Color(0, 255, 0)
CERVENA = Color(255, 0, 0)
okno = display.set_mode([1000, 800])


# 4. ak sa nezrážajú tak oba zafarbíme na zeleno
xn = 0
yn = 0
vx = 0
vy = 0

while True:
    # 2. hrac = stvorec, sa pohybuje šípkami
    krok = 5
    klavesnica = event.poll()
    if klavesnica.type == KEYDOWN:
        if klavesnica.key == K_LEFT:
            vx = -krok
        if klavesnica.key == K_RIGHT:
            vx = krok
        if klavesnica.key == K_UP:
            vy = -krok
        if klavesnica.key == K_DOWN:
            vy = krok
    if klavesnica.type == KEYUP:
        vx = 0
        vy = 0

    xn = xn + vx
    yn = yn + vy

    okno.fill(BIELA)
    # Kreslenie
    # 1. pevny štvorec nakresliť
    xp = 250
    yp = 400
    a = 50
    r = 50

    # 3. ak sa "zrazia", tak oba zafarbíme na červeno
    # Nezrazia
    if sqrt((xp - xn) ** 2 + (yp - yn) ** 2) >= 2 * r:
        draw.circle(okno, ZELENA, [xp, yp], a)
        draw.circle(okno, ZELENA, [xn, yn], a)
    else:
        draw.circle(okno, CERVENA, [xp, yp], a)
        draw.circle(okno, CERVENA, [xn, yn], a)

    """
    if ((xn - r) + a < (xp - r) or (xp - r) + a < (xn - r)) or ((yn - r) + a < (yp - r) or (yp - r) + a < (yn - r)):
        draw.circle(okno, ZELENA, [xp, yp], a)
        draw.circle(okno, ZELENA, [xn, yn], a)
    else:
        draw.circle(okno, CERVENA, [xp, yp], a)
        draw.circle(okno, CERVENA, [xn, yn], a)
    """
    """
    if (xn + a < xp or xp + a < xn) or (yn + a < yp or yp + a < yn):
        draw.rect(okno, ZELENA, Rect([xp, yp], [a, a]))
        draw.rect(okno, ZELENA, Rect([xn, yn], [a, a]))
    else:
        draw.rect(okno, CERVENA, Rect([xp, yp], [a, a]))
        draw.rect(okno, CERVENA, Rect([xn, yn], [a, a]))
    """
    display.update()
    time.delay(10)



