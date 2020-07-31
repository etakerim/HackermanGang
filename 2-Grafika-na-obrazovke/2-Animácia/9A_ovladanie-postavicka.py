from pygame import *

CERVENA = Color(255, 0, 0)
CIERNA = Color(0, 0, 0)

ROZLISENIE = [1000, 800]
okno = display.set_mode(ROZLISENIE)

robot = image.load("robot.png").convert_alpha()
robot = transform.scale(robot, [100, 100])

x = 500
y = 400
vx = 0
vy = 0

while True:
    okno.fill(CIERNA)
    klavesnica = event.poll()
    if klavesnica.type == KEYDOWN:
        if klavesnica.key == K_LEFT:
            vx = -5
        if klavesnica.key == K_RIGHT:
            vx = 5
        if klavesnica.key == K_DOWN:
            vy = 5
        if klavesnica.key == K_UP:
            vx = -5
    if klavesnica.type == KEYUP:
        vx = 0
        vy = 0

    x = x + vx
    y = y + vy

    okno.blit(robot, [x, y])
    #draw.circle(okno, CERVENA, [x,  y], 50)
    display.update()
    time.delay(10)