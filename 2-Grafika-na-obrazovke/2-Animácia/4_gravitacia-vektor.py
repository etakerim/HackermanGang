from pygame import *

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
WIDTH = 400
HEIGHT = 800
R = 20

r = Vector2([WIDTH / 2, -R])
v = Vector2([0, 0])
a = Vector2([0, 0.4])

screen = display.set_mode((WIDTH, HEIGHT))
while True:
    v = v + a
    r = r + v

    screen.fill(BLACK)
    draw.circle(screen, RED, (int(r.x), int(r.y)), R)
    display.update()
    time.delay(16)
