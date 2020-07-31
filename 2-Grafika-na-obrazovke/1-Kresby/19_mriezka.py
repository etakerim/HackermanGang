from pygame import *

COLOR = Color(0, 0, 0)
RED = Color(255, 0, 0)
okno = display.set_mode([900, 600])

doska = [
    ["-", "-", "*", "*", "-", "*"],
    ["-", "-", "-", "*", "-", "*"],
    ["-", "-", "*", "*", "-", "*"],
    ["-", "-", "*", "*", "-", "*"],
]

x = 0
y = 0

n = 6
a = 900 // n
okno.fill(Color(255, 255, 255))

for j in range(4):
    # 1. riadok
    for i in range(6):
        if doska[j][i] == "*":
            draw.rect(okno, RED, Rect([x + a * i, y + a * j], [a, a]))
        if doska[j][i] == "-":
             draw.rect(okno, COLOR, Rect([x + a * i, y + a * j], [a, a]), 3)

while True:
    display.update()