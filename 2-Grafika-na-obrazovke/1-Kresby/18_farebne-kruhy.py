from pygame import *

MODRA = Color(0, 0, 255)
ZELENA = Color(0, 255, 0)

ROZLISENIE = [600, 400]
okno = display.set_mode(ROZLISENIE)

draw.rect(okno, MODRA, Rect([100, 100], [50, 30]))
draw.rect(okno, MODRA, [[100, 100], [50, 30]])

while True:
    udalost = event.poll()
    if udalost.type == MOUSEBUTTONDOWN:
        if udalost.button == 1:
            x = udalost.pos[0]
            y = udalost.pos[1]

            farba = MODRA
            if x < 300:
                farba = ZELENA
            draw.circle(okno, farba, [x, y], 50)

    display.update()