from pygame import *
from random import *

WIDTH = 400
HEIGHT = 400
R = 4

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
TREE_COLOR = Color(85, 230, 205)

tree = [Vector2(WIDTH / 2, HEIGHT / 2)]

def random_place():
    edge = randrange(4)
    if edge == 0:
        return Vector2(randrange(WIDTH), 0)
    elif edge == 1:
        return Vector2(randrange(WIDTH), HEIGHT)
    elif edge == 2:
        return Vector2(0, randrange(HEIGHT))
    elif edge == 3:
        return Vector2(WIDTH, randrange(HEIGHT))

walkers = []
for i in range(200):
    walkers.append(random_place())

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    for i in range(50):
        for dot in walkers:
            stuck = False
            for node in tree:
                if dot.distance_squared_to(node) < 4*R*R:
                    stuck = True
                    break

            if stuck:
                tree.append(dot)
                walkers.remove(dot)
            else:
                velocity = Vector2()
                velocity.from_polar((3, randrange(360)))

                dot += velocity
                dot.x = min(WIDTH, max(0, dot.x))
                dot.y = min(HEIGHT, max(0, dot.y))

    #while len(walkers) < 200:
    #    walkers.append(random_place())

    screen.fill(BLACK)
    for dot in walkers:
        draw.circle(screen, WHITE, [int(dot.x), int(dot.y)], R)

    for node in tree:
        draw.circle(screen, TREE_COLOR, [int(node.x), int(node.y)], R)
    display.update()
    time.delay(16)