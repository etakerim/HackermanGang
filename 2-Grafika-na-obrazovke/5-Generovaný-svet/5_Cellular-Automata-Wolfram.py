from pygame import *

WIDTH = 600
HEIGHT = 800
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

def rules(a, b, c):
    ruleset = 90
    a = (a & 1) << 2
    b = (b & 1) << 1
    c = (c & 1)
    return (ruleset >> (a | b | c)) & 1

w = 10

cells = []
for i in range(WIDTH // w):
    cells.append(0)
cells[len(cells) // 2] = 1

screen = display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
while True:
    # print(cells)
    # Všetko skopírujem o jeden riadok vyššie
    scroll = Surface([WIDTH, HEIGHT - w])
    scroll.blit(screen, (0, 0), (0, w, WIDTH, HEIGHT))
    screen.fill(WHITE)
    screen.blit(scroll, (0, 0))

    # Pridám spodný riadok
    for i in range(len(cells)):
        color = BLACK if cells[i] == 1 else WHITE
        draw.rect(screen, color, (i * w, HEIGHT - w, w, w))

    nextgen = []
    for i in range(len(cells)):
        x = rules(cells[(i-1) % len(cells)], cells[i], cells[(i+1) % len(cells)])
        nextgen.append(x)

    cells = nextgen
    display.update()
    time.delay(30)