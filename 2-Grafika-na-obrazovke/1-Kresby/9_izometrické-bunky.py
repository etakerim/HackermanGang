from pygame import *

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)

WIDTH = 512
HEIGHT = 480

tile = Vector2(40, 20)
origin = Vector2(5, 1)

def to_screen(v):
    return Vector2(
        v.x * tile.x / 2 - v.y * tile.x / 2 + origin.x * tile.x,
        v.x * tile.y / 2 + v.y * tile.y / 2 + origin.y * tile.y
    )

screen = display.set_mode([WIDTH, HEIGHT])

world = []  # 10x14
for r in range(10):
    world.append([])
    for s in range(14):
        world[r].append(0)


while True:
    screen.fill(WHITE)
    # Rendrovanie odzadu dopredu
    for y in range(len(world)):
        for x in range(len(world[y])):
            w = to_screen(Vector2(x, y))
            points = [
                [int(w.x + tile.x / 2), int(w.y)],
                [int(w.x + tile.x), int(w.y + tile.y / 2)],
                [int(w.x + tile.x / 2), int(w.y + tile.y)],
                [int(w.x), int(w.y + tile.y / 2)]
            ]
            draw.polygon(screen, BLACK, points, 1)

    event.poll()
    m = Vector2(mouse.get_pos())
    cell = Vector2(m.x // tile.x, m.y // tile.y)
    offset = Vector2(m.x % tile.x, m.y % tile.y)

    draw.rect(screen, RED, Rect([int(cell.x * tile.x), int(cell.y * tile.y)], [int(tile.x), int(tile.y)]), 1)

    selected = Vector2(
        (cell.y - origin.y) + (cell.x - origin.x),
        (cell.y - origin.y) - (cell.x - origin.x)
    )

    s = to_screen(selected)

    points = [
        [int(s.x + tile.x / 2), int(s.y)],
        [int(s.x + tile.x), int(s.y + tile.y / 2)],
        [int(s.x + tile.x / 2), int(s.y + tile.y)],
        [int(s.x), int(s.y + tile.y / 2)]
    ]
    draw.polygon(screen, YELLOW, points)

    display.update()
    time.delay(20)


# Cx = Mx div Tw
# Cy = My div Tw

# Ox = Mx mod Tw
# Oy = My mod Tw

# i = Cy * width + Cx

