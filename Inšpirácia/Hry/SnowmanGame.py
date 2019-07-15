import pygame
import random


def constrain(x, min, max):
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x


class Entity:
    def __init__(self, x, y, w, h, step):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.step = step

    def move(self, dx, dy):
        self.x += dx * self.step
        self.y += dy * self.step

    def collides(self, other):
        a = pygame.Rect(self.x, self.y, self.w, self.h)
        b = pygame.Rect(other.x, other.y, other.w, other.h)
        return a.colliderect(b)


class Cannon(Entity):
    def __init__(self, x, y, w, h, step):
        super().__init__(x, y, w, h, step)
        self.COLOR = (85, 50, 5)

    def draw(self, canvas):
        pos = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(canvas, self.COLOR, pos)


class Snowman(Entity):
    def __init__(self, x, y, h, step):
        HDIV = h / 18
        self.R_SPHERES = [int(HDIV * 2.4), int(HDIV * 3.2), int(HDIV * 4.2)]
        self.Y_CENTER = [int(HDIV * 2.4), int(HDIV * 7.2), int(HDIV * 14)]
        super().__init__(x, y, 2 * max(self.R_SPHERES), h, step)

    def draw(self, canvas):
        body = (240, 240, 240)
        coal = (0, 0, 0)
        carrot = (250, 120, 5)
        xmid = self.x + self.w // 2
        rb = self.w // 16

        # Snehové guľe
        for y, r in zip(self.Y_CENTER, self.R_SPHERES):
            pygame.draw.circle(canvas, body, (xmid, self.y + y), r)

        # Oči
        rhalf = self.R_SPHERES[0] // 2
        rthird = self.R_SPHERES[0] // 3
        y = self.y + self.Y_CENTER[0] - rhalf

        pygame.draw.rect(canvas, coal, (xmid - rhalf, y, rb, rb))
        pygame.draw.rect(canvas, coal, (xmid + rhalf, y, rb, rb))

        # Mrkva
        points = [
                (xmid, self.y + self.Y_CENTER[0] - rthird),
                (xmid, self.y + self.Y_CENTER[0] + rthird),
                (xmid + self.w // 3, self.y + self.Y_CENTER[0])]
        pygame.draw.polygon(canvas, carrot, points)

        # Gombíky
        for y, r in zip(self.Y_CENTER[1:], self.R_SPHERES[1:]):
            b = 2 * r // 3
            for yb in range(-b, b + 1, b):
                pos = (xmid - rb, self.y + y + yb - rb, rb, rb)
                pygame.draw.rect(canvas, coal, pos)


class Bullet(Entity):
    def __init__(self, x, y, step):
        super().__init__(x, y, 10, 10, step)
        self.COLOR = (210, 35, 0)

    def draw(self, canvas):
        pos = (self.x, self.y, self.w, self.h)
        pygame.draw.ellipse(canvas, self.COLOR, pos)


class Score:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.points = 0
        self.COLOR = (10, 0, 100)
        self.font = pygame.font.SysFont('opensans', 40)
        self.texture = self.font.render(str(self.points), True, self.COLOR)

    def gain(self, n):
        self.points += n
        self.texture = self.font.render(str(self.points), True, self.COLOR)

    def draw(self, canvas):
        canvas.blit(self.texture, (self.x, self.y))


class SnowmanGame:
    def __init__(self, w, h):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((w, h))
        pygame.display.set_caption('Snehuliaci útočia')

        self.running = True
        self.BGCOLOR = (190, 215, 255)
        self.w, self.h = self.window.get_size()

        self.GENERATE_SNOWMAN = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GENERATE_SNOWMAN, 2000)
        self.on_init()

    def on_init(self):
        self.score = Score(self.w - 50, 20)
        self.cannon = Cannon(self.w // 2, self.h - 50, 30, 50, step=4)
        self.bullets = []
        self.snowmans = []

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(x=self.cannon.x + self.cannon.w // 2,
                                y=self.cannon.y, step=6)
                self.bullets.append(bullet)

        elif event.type == self.GENERATE_SNOWMAN:
            snowman = Snowman(x=random.randint(50, self.w - 50), y=-100,
                              h=80, step=3)
            self.snowmans.append(snowman)

    def on_key_hold(self, keys):
        if keys[pygame.K_LEFT]:
            self.cannon.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.cannon.move(1, 0)
        self.cannon.x = constrain(self.cannon.x, 0, self.w - self.cannon.w)

    def on_calculate(self):
        for b in self.bullets[:]:
            if b.y - b.h < 0:
                self.bullets.remove(b)

            for s in self.snowmans[:]:
                if b.collides(s):
                    self.score.gain(1)
                    self.bullets.remove(b)
                    self.snowmans.remove(s)
                    break

        for s in self.snowmans:
            if s.y + s.h > self.cannon.y:
                return self.on_init()

    def on_render(self):
        self.window.fill(self.BGCOLOR)

        self.score.draw(self.window)
        self.cannon.draw(self.window)

        for bullet in self.bullets:
            bullet.move(0, -1)
            bullet.draw(self.window)

        for snowman in self.snowmans:
            snowman.move(0, 1)
            snowman.draw(self.window)

    def play(self):
        timer = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_key_hold(pygame.key.get_pressed())
            self.on_calculate()
            self.on_render()

            timer.tick(60)
            pygame.display.update()

        pygame.font.quit()
        pygame.quit()


game = SnowmanGame(800, 500)
game.play()
