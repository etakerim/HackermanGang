from pygame import *
from random import *

WIDTH = 400
HEIGHT = 400
R = 4

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
TREE_COLOR = Color(85, 230, 205)
ITER = 50
WALKERS = 50

tree = []
for x in range(0, WIDTH, 2*R):
    tree.append(Vector2(x, HEIGHT))

walkers = []
for i in range(WALKERS):
    walkers.append(Vector2(randrange(HEIGHT), 0))

screen = display.set_mode((WIDTH, HEIGHT))
while True:
    for i in range(ITER):
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
                dot += Vector2(uniform(-1, 1), uniform(-0.5, 1))
                dot.x = min(WIDTH, max(0, dot.x))
                dot.y = min(HEIGHT, max(0, dot.y))

    while len(walkers) < WALKERS:
        walkers.append(Vector2(randrange(HEIGHT), 0))

    screen.fill(BLACK)
    for dot in walkers:
        draw.circle(screen, WHITE, [int(dot.x), int(dot.y)], R)

    for node in tree:
        draw.circle(screen, TREE_COLOR, [int(node.x), int(node.y)], R)
    display.update()
    time.delay(16)