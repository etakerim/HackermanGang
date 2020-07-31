from pygame import *
from random import *

WIDTH = 800
HEIGHT = 600

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
R = 2

location = Vector2([randrange(WIDTH), randrange(HEIGHT)])
velocity = Vector2([0, 0])
acceleration = Vector2([0, 0])
mous = Vector2([0, 0])

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    ev = event.poll()
    if ev.type == MOUSEMOTION:
        mous = Vector2(ev.pos)

    direction = mous - location
    direction = 0.5 * direction.normalize()
    acceleration = direction

    velocity += acceleration
    velocity.scale_to_length(min(max(4, velocity.magnitude()), 8))
    location += velocity

    # screen.fill(BLACK)  Čo keby vymažem a zväčším polomer
    draw.circle(screen, RED, (int(location.x), int(location.y)), R)
    display.update()
    time.delay(10)