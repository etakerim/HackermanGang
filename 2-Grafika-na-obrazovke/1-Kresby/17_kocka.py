from pygame import *
from random import *

okno = display.set_mode([800, 600])
CIERNA = Color(0, 0, 0)
BIELA = Color(255, 255, 255)

# Premenné podľa ktorých nakreslíme kocku (pozícia a rozmer)
X = 200
Y = 200
A = 300

while True:
    # Vypýtame si poslednú akciu, ktorú používateľ vykonal.
    udalost = event.poll()
    # Zaujíma nás stlačenie ľavého tlačidla na myši
    if udalost.type == MOUSEBUTTONDOWN and udalost.button == 1:
        # Nakreslíme štvorec, ktorý ohraničuje bodky na kocke
        okno.fill(BIELA)
        draw.rect(okno, CIERNA, Rect([X, Y], [A, A]), 4)

        # Hod kockou: randint(1, 5) vytvorí náhodné číslo medzi 1 - 5
        hod = randint(1, 5)

        # Podľa hodnoty hodu sa rozhodneme, ktoré bodky nakresliť
        if hod == 1:
            draw.rect(okno, CIERNA, Rect([X + A * (3 / 7), Y + A * (3 / 7)], [A // 7, A // 7]))

        if hod == 2:
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))

        if hod == 3:
            draw.rect(okno, CIERNA, Rect([X + A * (3 / 7), Y + A * (3 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))

        if hod == 4:
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))

        if hod == 5:
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (1 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (1 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (5 / 7), Y + A * (5 / 7)], [A // 7, A // 7]))
            draw.rect(okno, CIERNA, Rect([X + A * (3 / 7), Y + A * (3 / 7)], [A // 7, A // 7]))

    display.update()