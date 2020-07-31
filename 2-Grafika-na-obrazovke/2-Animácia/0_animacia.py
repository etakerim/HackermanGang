from pygame import *

BIELA = Color(255, 255, 255)
CIERNA = Color(0, 0, 0)
okno = display.set_mode([800, 600])

# Počiatočné vlastnosti guličky
x = 100
y = 300
r = 20

# Informácie o pohybe
vx = 3
ax = 1

while True:
    # Vymazanie okna pre čistý snímok
    okno.fill(CIERNA)
    # Pohyb
    x = x + vx
    vx = vx + ax

    # Odrážanie
    if x + r > 800:
        vx = -vx
    if x - r < 0:
        vx = -vx

    # Prekreslenie
    draw.circle(okno, BIELA, [x, y], r)
    # Spomalenie animácie
    time.delay(20)
    display.update()