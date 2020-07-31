from pygame import *

WHITE = Color(255, 255, 255)
BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)


canvas = display.set_mode([800, 400])

def rhombus(x_inc):
    r = 5
    ax = 20
    ay = canvas.get_height() // 2

    for i in range(1, 9):
        for y in range(8):
            draw.circle(canvas, BLUE, [ax, ay], r)
            ax += x_inc
            ay -= 25

        ax = 20 + i * x_inc
        ay = (canvas.get_height() // 2) + i * 25

rhombus(50)
display.update()

while True:
    time.delay(30)
