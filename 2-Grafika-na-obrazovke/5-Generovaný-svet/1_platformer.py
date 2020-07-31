# https://www.youtube.com/watch?v=oJvJZNyW_rw
from pygame import *

w_level = 64
h_level = 16
level  = "................................................................"
level += "................................................................"
level += "................................................................"
level += "................................................................"
level += "......................########.................................."
level += ".........#...........###........................................"
level += "...................###.........................................."
level += "..................####.........................................."
level += "#######################################.#############......#####"
level += "......................................#.#...............###....."
level += "........................###############.#............###........"
level += "........................#...............#.........###..........."
level += "........................#.###############......###.............."
level += "........................#...................###................."
level += "........................####################...................."
level += "................................................................"

def get_tile(x, y):
    global level, w_level, h_level
    x, y = int(x), int(y)
    if 0 <= x < w_level and 0 <= y < h_level:
        return level[y * w_level + x]
    return " "

def set_tile(x, y, c):
    global level, w_level, h_level
    x, y = int(x), int(y)
    if 0 <= x < w_level and 0 <= y < h_level:
        level[y * w_level + x] = c

WIDTH = 900
HEIGHT = 600
w_tile = 50
h_tile = 50
visible_tilesX = WIDTH // w_tile
visible_tilesY = HEIGHT // h_tile

cameraX = 0
cameraY = 0

playerX = 0
playerY = 0

screen = display.set_mode([WIDTH, HEIGHT])
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
CYAN = Color(0, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)

playerVelX = 0
playerVelY = 0
step = 1

while True:
    ev = event.poll()
    if ev.type == KEYDOWN:
        if ev.key == K_UP:
            playerVelY = -step
        elif ev.key == K_DOWN:
            playerVelY = step
        elif ev.key == K_RIGHT:
            playerVelX = step
        elif ev.key == K_LEFT:
            playerVelX = -step
    if ev.type == KEYUP:
        playerVelX = 0
        playerVelY = 0

    # Collisions: Without obstacles this would be final position after move
    newPlayerX = playerX + playerVelX
    newPlayerY = playerY + playerVelY
    print(newPlayerX, newPlayerY)

    if playerVelX <= 0:
        if get_tile(newPlayerX, playerY) != "." or get_tile(newPlayerX, playerY + 0.9) != ".":
            newPlayerX = int(newPlayerX) + 1
            playerVelX = 0
    else:
        if get_tile(newPlayerX + 1, playerY) != "." or get_tile(newPlayerX + 1, playerY + 0.9) != ".":
            newPlayerX = int(newPlayerX)
            playerVelX = 0

    if playerVelY <= 0:
        if get_tile(newPlayerX, newPlayerY) != "." or get_tile(newPlayerX + 0.9, newPlayerY) != ".":
            newPlayerY = int(newPlayerY) + 1
            playerVelY = 0
    else:
        if get_tile(newPlayerX, newPlayerY + 1) != "." or get_tile(newPlayerX + 0.9, newPlayerY + 1) != ".":
            newPlayerY = int(newPlayerY)
            playerVelY = 0


    playerX = newPlayerX
    playerY = newPlayerY

    cameraX = playerX
    cameraY = playerY

    # Draw level
    # Top-leftmost visible tile
    offsetX = cameraX - visible_tilesX / 2
    offsetY = cameraY - visible_tilesY / 2
    # Clamp camera to game boundaries
    if offsetX < 0: offsetX = 0
    if offsetY < 0: offsetY = 0
    if offsetX > w_level - visible_tilesX: offsetX = w_level - visible_tilesX
    if offsetY > h_level - visible_tilesY: offsetY = h_level - visible_tilesY

    # Get offsets for smooth movement (partial tile percentages based on position)
    tileOffsetX = (offsetX - int(offsetX)) * w_tile
    tileOffsetY = (offsetY - int(offsetY)) * h_tile

    screen.fill(BLACK)
    for x in range(-1, visible_tilesX + 1):
        for y in range(-1, visible_tilesY + 1):
            tileID = get_tile(x + offsetX, y + offsetY)
            region = Rect(
                [int(x * w_tile - tileOffsetX), int(y * h_tile - tileOffsetY)],
                [int(w_tile - tileOffsetX), int(h_tile - tileOffsetY)]
            )
            if tileID == ".":
                screen.fill(CYAN, region)
            elif tileID == "#":
                screen.fill(RED, region)
    # Draw Player
    screen.fill(GREEN, Rect([int((playerX - offsetX) * w_tile), int((playerY - offsetY) * h_tile)], [w_tile, h_tile]))

    display.update()
    time.delay(60)