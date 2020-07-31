from pygame import *

BLACK = Color(0, 0, 0)
WIDTH = 600
HEIGHT = 400
screen = display.set_mode([WIDTH, HEIGHT])

x = WIDTH // 2
y = HEIGHT // 2
h = 30
step = 5

robot = image.load("images/robot.png").convert_alpha()
robot = transform.scale(robot, [2*h, 2*h])

background = image.load("images/park.png").convert()
background = transform.scale(background, [WIDTH, HEIGHT])

vx = 0
vy = 0

while True:
    for ev in event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_RIGHT:
                vx = step
            elif ev.key == K_LEFT:
                vx = -step
            elif ev.key == K_UP:
                vy = -step
            elif ev.key == K_DOWN:
                vy = step
        elif ev.type == KEYUP:
            if (ev.key == K_RIGHT or
                    ev.key == K_LEFT or
                    ev.key == K_UP or
                    ev.key == K_DOWN):
                vx = 0
                vy = 0

    x = (x + vx) %  WIDTH
    y = (y + vy) % HEIGHT

    # screen.fill(BLACK)
    screen.blit(background, [0, 0])
    screen.blit(robot, [x-h, y-h])
    display.update()
    time.delay(10)