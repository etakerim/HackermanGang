import pygame
from random import randrange

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))

for angle in range(360):
    v = pygame.Vector2()
    v.from_polar((100, angle))

    color = pygame.Color(0, 0, 0)
    color.hsva = (angle, 100, 100)

    pygame.draw.line(screen, color, (300, 300), (300 + int(v.x), 300 + int(v.y)),3)
    #pygame.display.update()
    #pygame.time.delay(16)

# Keď dáme update sem nakreslí sa naraz
pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        center = pygame.Vector2(300, 300)
        mouse = pygame.Vector2(event.pos)
        direction = mouse - center
        r, angle = direction.as_polar()
        if angle < 0:
            angle = 180 + (180 - abs(angle))

        print(r, angle)

        if r <= 100:
            pick = pygame.Color(0,0,0)
            pick.hsva = (angle, 100, r)
            pygame.draw.rect(screen, pick, (0, 0, 100, 100))
            pygame.display.update()