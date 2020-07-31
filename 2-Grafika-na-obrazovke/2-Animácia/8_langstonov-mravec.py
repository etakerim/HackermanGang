from pygame import *

WIDTH = 600
HEIGHT = 400

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

screen = display.set_mode([WIDTH, HEIGHT])

x = WIDTH // 2
y = HEIGHT // 2
dire = 0
# Create: Turmite
while True:
    # "RL" Langston Ant
    for i in range(100):
        cell = screen.get_at((x, y))
        if cell == WHITE:
            screen.set_at((x, y), BLACK)
            dire = abs((dire + 1) % 4)
        elif cell == BLACK:
            screen.set_at((x, y), WHITE)
            dire = abs((dire - 1) % 4)

        if dire == 0:
            y -= 1
        elif dire == 1:
            x += 1
        elif dire == 2:
            y += 1
        elif dire == 3:
            x -= 1

        x %= WIDTH
        y %= HEIGHT

    display.update()
    time.delay(16)