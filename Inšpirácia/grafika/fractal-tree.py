import pygame

width = 400
height = 400
WHITE = (255, 255, 255)
BGC = (51, 51, 51)
angle = 30
window = pygame.display.set_mode((width, height))

def branch(a, v):
    if v.length() > 2:
        b = a + (v.elementwise() * pygame.math.Vector2(1, -1))
        pygame.draw.line(window, WHITE, (a.x, a.y), (b.x, b.y))
        branch(b, v.rotate(angle) * 0.67)
        branch(b, v.rotate(-angle) * 0.67)

window.fill(BGC)
branch(pygame.math.Vector2(200, height),
       pygame.math.Vector2(0, 80))

timer = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    timer.tick(30)