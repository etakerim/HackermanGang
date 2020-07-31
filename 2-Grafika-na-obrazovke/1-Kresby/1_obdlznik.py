from pygame import *

# Vytvor okno
screen = display.set_mode([640, 480])
# Biela farba
WHITE = Color(255, 255, 255)
# Oblasť - pozícia [100, 100] a rozmery 50x50
AREA = Rect([100, 100], [50, 50])

# Nakresli odĺžnik na obrazovku bielou farbou
# do obdĺžnikovej oblasti AREA
draw.rect(screen, WHITE, AREA)

# Zobraz kresby v okne
display.update()

while True:
    e = event.poll()
    if e.type == QUIT:
        break