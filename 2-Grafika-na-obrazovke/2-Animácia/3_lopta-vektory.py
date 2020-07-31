from pygame import *

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
WIDTH = 600
HEIGHT = 400
r = 20

pos = Vector2([r, r])
velocity = Vector2([5, 5])

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    # Zmeň polohu podľa rýchlosti
    pos = pos + velocity

    # Uprav vektor rýchlosti
    if pos.x - r < 0 or pos.x + r > WIDTH:
        velocity.x = -velocity.x
    if pos.y - r < 0 or pos.y + r > HEIGHT:
        velocity.y = -velocity.y

    # Nakresli
    screen.fill(BLACK)
    draw.circle(screen, RED, (int(pos.x), int(pos.y)), r)
    display.update()
    time.delay(16)