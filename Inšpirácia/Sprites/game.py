import pygame
import sys
import random


WIDTH = 800
HEIGHT = 500
FRAME_COUNT = 12
FRAME_WIDTH = 80
FRAME_HEIGHT = 100
WHITE = (255, 255, 255)

class Sprite:
    def __init__(self, x, y, speed, animation):
        self.x = x
        self.y = y
        self.speed = speed
        self.animation = animation
        self.index = 0

    def draw(self, window):
        i = int(self.index) % len(self.animation)
        window.blit(self.animation[i], (self.x, self.y))
    
    def animate(self):
        self.index += self.speed
        self.x += self.speed * 5
        if self.x > WIDTH:
            self.x = -FRAME_WIDTH


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

spritesheet = pygame.image.load('stickmen.png').convert_alpha()
sx, sy, sw, sh = spritesheet.get_rect() 

animation = []
for x in range(0, sw, FRAME_WIDTH):
    frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)    
    frame.blit(spritesheet, (0, 0), pygame.Rect(x, 0, FRAME_WIDTH, FRAME_HEIGHT))
    animation.append(frame)

runners = []
for y in range(0, HEIGHT, FRAME_HEIGHT):
    rnd = random.random() + 0.7
    s = Sprite(0, y, rnd, animation)
    runners.append(s)


timer = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill(WHITE)

    for runner in runners:
        runner.draw(window)
        runner.animate()

    pygame.display.update()
    timer.tick(30)
