import pygame
import copy
from random import randrange

WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

res = 10
stlpce = WIDTH // res
riadky = HEIGHT // res

def susedia(grid, r, s):
    suma = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = (r+i+riadky) % riadky
            col = (s+j+stlpce) % stlpce
            suma += grid[row][col]
    suma -= grid[r][s]
    return suma

world = []
for i in range(riadky):
    world.append([])
    for j in range(stlpce):
        world[i].append(randrange(2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
while True:
    screen.fill(WHITE)
    for r in range(riadky):
        for s in range(stlpce):
            color = BLACK if world[r][s] == 1 else WHITE
            pygame.draw.rect(screen, BLACK, (s * res, r * res, res, res), 2)
            screen.fill(color, (s * res, r * res, res - 1, res - 1))


    newgen = []
    for r in range(riadky):
        newgen.append([])
        for s in range(stlpce):
            neighbors = susedia(world, r, s)

            state = world[r][s]
            if state == 0 and neighbors == 3 :
                newgen[r].append(1)
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                newgen[r].append(0)
            else:
                newgen[r].append(state)

    world = copy.deepcopy(newgen)
    pygame.display.update()
    pygame.time.delay(100)