from pygame import *
from random import *

WIDTH = 600
HEIGHT = 400
BLACK = Color(0, 0, 0)

particles = []

screen = display.set_mode([WIDTH, HEIGHT])
while True:
    for p in particles:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["c"] -= 2
        if p["y"] < 0 or p["c"] < 0:
            particles.remove(p)

    for i in range(5):
        p = {
            "x": 300,
            "y": 380,
            "vx": uniform(-1, 1),
            "vy": uniform(-3, -1),
            "c": 255
        }
        particles.append(p)

    screen.fill(BLACK)
    for p in particles:
        draw.circle(screen, Color(p["c"], p["c"], p["c"]), (int(p["x"]), int(p["y"])), 8)
    display.update()
    time.delay(16)