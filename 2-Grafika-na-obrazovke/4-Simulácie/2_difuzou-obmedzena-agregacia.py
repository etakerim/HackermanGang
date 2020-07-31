from pygame import *
from random import *

WIDTH = 400
HEIGHT = 400
R = 4

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
TREE_COLOR = Color(85, 230, 205)

seed = Vector2([WIDTH / 2, HEIGHT / 2])
tree = [seed]

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    walker = Vector2([randrange(WIDTH), randrange(HEIGHT)])
    stuck = False

    while not stuck:
        for node in tree:
            if walker.distance_squared_to(node) < 4*R*R:
                stuck = True
                break

        velocity = Vector2()
        velocity.from_polar((1, randrange(360)))

        walker += velocity
        walker.x = min(WIDTH, max(0, walker.x))
        walker.y = min(HEIGHT, max(0, walker.y))

    tree.append(walker)

    for node in tree:
        draw.circle(screen, TREE_COLOR, (int(node.x), int(node.y)), R)
    display.update()
    time.delay(16)