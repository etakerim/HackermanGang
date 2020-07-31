from pygame import *

WIDTH = 600
HEIGHT = 400

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
r = 20

center = Vector2(WIDTH // 2, HEIGHT // 2)
mys = Vector2(WIDTH // 2, HEIGHT // 2)

screen = display.set_mode((WIDTH, HEIGHT))
while True:
    e = event.poll()
    if e.type == MOUSEMOTION:
        mys = Vector2(e.pos)
        mys -= center
        mys.scale_to_length(100)
        mys += center

    screen.fill(BLACK)
    draw.line(screen, WHITE, (int(center.x), int(center.y)),
                             (int(mys.x), int(mys.y)))
    display.update()