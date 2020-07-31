from pygame import *
from random import randrange

"""
Recursive backtracker
https://en.wikipedia.org/wiki/Maze_generation_algorithm

The depth-first search algorithm of maze generation is frequently implemented using backtracking.
This can be described with a following recursive routine:

    Choose the initial cell, mark it as visited and push it to the stack
    While the stack is not empty
        Pop a cell from the stack and make it a current cell
        If the current cell has any neighbours which have not been visited
            Push the current cell to the stack
            Choose one of the unvisited neighbours
            Remove the wall between the current cell and the chosen cell
            Mark the chosen cell as visited and push it to the stack
"""

WHITE = Color(255, 255, 255)
BG = Color(50, 50, 50)

WIDTH = 601
HEIGHT = 601

screen = display.set_mode([WIDTH, HEIGHT])
riadky = 20
stlpce = 20
a = HEIGHT // riadky
b = WIDTH // stlpce

maze = []
for y in range(riadky):
    maze.append([])
    for x in range(stlpce):
        cell = {   # policko
            "x": x,
            "y": y,
            "walls": [True, True, True, True],
            "visited": False
        }
        maze[y].append(cell)

stack = []

current = maze[0][0]
current["visited"] = True
stack.append(current)

while len(stack) > 0:
    current = stack.pop()
    r = current["y"]
    s = current["x"]

    susedia = []
    if (0 <= r-1 < riadky and maze[r - 1][s]["visited"] == False):
        susedia.append(maze[r - 1][s])
    if (0 <= s+1 < stlpce and maze[r][s + 1]["visited"] == False):
        susedia.append(maze[r][s + 1])
    if (0 <= r+1 < riadky and maze[r + 1][s]["visited"] == False):
        susedia.append(maze[r + 1][s])
    if (0 <= s-1 < stlpce and maze[r][s - 1]["visited"] == False):
        susedia.append(maze[r][s - 1])

    if len(susedia) > 0:
        # STEP 1
        stack.append(current)
        # STEP 2
        step = susedia[randrange(len(susedia))]

        # STEP 3
        xsmer = step["x"] - current["x"]
        if xsmer == 1:
            current["walls"][1] = False
            step["walls"][3] = False
        elif xsmer == -1:
            current["walls"][3] = False
            step["walls"][1] = False

        ysmer = step["y"] - current["y"]
        if ysmer == 1:
            current["walls"][2] = False
            step["walls"][0] = False
        elif ysmer == -1:
            current["walls"][0] = False
            step["walls"][2] = False

        # STEP 4
        step["visited"] = True
        stack.append(step)
        current = step

    # Nakresli bludisko
    screen.fill(BG)
    for r in range(riadky):
        for s in range(stlpce):
            cell = maze[r][s]
            walls = cell["walls"]

            x = s * a
            y = r * a
            if walls[0]:
                draw.line(screen, WHITE, [x, y], [x + b, y])          # N
            if walls[1]:
                draw.line(screen, WHITE, [x + b, y], [x + b, y + a])  # E
            if walls[2]:
                draw.line(screen, WHITE, [x + b, y + a], [x, y + a])  # S
            if walls[3]:
                draw.line(screen, WHITE, [x, y + a], [x, y])          # W

            #if cell["visited"]:
            #    draw.rect(screen, Color(200, 0, 200), Rect([x, y], [a, b]))

    display.update()
    time.delay(30)