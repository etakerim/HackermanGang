import pygame
import noise

width = 300
height = 300
WHITE = (255, 255, 255)
window = pygame.display.set_mode((width, height))


timer = pygame.time.Clock()
running = True
z = 0
scale = 50
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pixels = pygame.PixelArray(window)
    for x in range(width):
        for y in range(height):
            n = noise.pnoise3(x / scale, y / scale, z, octaves=6)
            n = (n + 1) * 128    
            pixels[x, y] = (n, n, n)
    z += 1 / scale
    del pixels
    pygame.display.update()
    timer.tick(30)
