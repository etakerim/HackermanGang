from pygame import *
from random import *

WIDTH = 256
HEIGHT = 256
BLOCK = 3
screen = display.set_mode([BLOCK * WIDTH, BLOCK * HEIGHT])

noise_seed = []
for i in range(WIDTH):
    noise_seed.append(random())

def perlin_noise_1d(seed, octaves, scaling_bias):
    output = []
    for x in range(len(seed)):
        noise = 0
        scale = 1
        scale_acc = 0
        pitch = len(seed)

        for o in range(octaves):
            sample1 = (x // pitch) * pitch
            sample2 = (sample1 + pitch) % len(seed)

            blend = (x - sample1) / pitch
            sample = (1 - blend) * seed[sample1] + blend * seed[sample2]
            noise += sample * scale

            scale_acc += scale
            scale /= scaling_bias
            pitch //= 2

        output.append(noise / scale_acc)
    return output

def generate(rate, scl):
    points = perlin_noise_1d(noise_seed, rate, scl)

    for i in range(len(points)):
        x = BLOCK * i
        y = BLOCK * int(HEIGHT // 2 - (points[i] * HEIGHT / 2))
        draw.rect(screen, Color(0, 255, 0), Rect([x, y], [BLOCK, BLOCK*HEIGHT // 2 - y]))

rate = 1
scl = 2
while True:
    for ev in event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                rate += 1
                if rate > 8:
                    rate = 1
            elif ev.key == K_UP:
                scl += 0.2
            elif ev.key == K_DOWN:
                scl -= 0.2
                if scl <= 0.2:
                    scl = 0.2
            screen.fill(Color(0, 0, 0))
            generate(rate, scl)

    display.update()
    time.delay(20)