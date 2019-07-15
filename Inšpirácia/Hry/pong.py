import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball:
    def __init__(self, x, y, speed):
        self.box = pygame.Rect(x, y, 15, 15)
        self.v = pygame.math.Vector2((speed, speed))
        # Add random start angle, player, that lost - move in oposite direction
        self.box_copy = self.box.copy()

    def reset(self):
        self.box = self.box_copy.copy()

    def redraw(self, window):
        self.box.x += self.v.x
        self.box.y += self.v.y
        pygame.draw.rect(window, WHITE, self.box)


class Player:
    def __init__(self, x, y, w, h):
        self.score = 0
        self.box = pygame.Rect(x, y, w, h)
        self.box_copy = self.box.copy()

    def reset(self):
        self.box = self.box_copy.copy()

    def move(self, window, step):
        self.box.y += step
        if self.box.y < 0:
            self.box.y = 0
        elif self.box.y + self.box.h > window.get_height():
            self.box.y = window.get_height() - self.box.h

    def redraw(self, window):
        pygame.draw.rect(window, WHITE, self.box)


class Game:
    def __init__(self, name, w, h):
        pygame.init()
        self.window = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.running = True
        self.ball = Ball(w // 2, h // 2, 5)
        self.player1 = Player(20, h // 2, 10, 80)
        self.player2 = Player(w - 30, h // 2, 10, 80)
        self.field = pygame.Rect(20, 0, w - 30, h)

    def reset(self):
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()

    def bounce(self):
        if (self.ball.box.colliderect(self.player1.box) or
                self.ball.box.colliderect(self.player2.box)):
            self.ball.v.x *= -1

        if (self.ball.box.y <= self.field.y or
                self.ball.box.y + self.ball.box.h >= self.window.get_height()):
            self.ball.v.y *= -1

    def score(self):
        compare = lambda p: p.box.x
        left = min(self.player1, self.player2, key=compare)
        right = max(self.player1, self.player2, key=compare)

        if self.ball.box.x < left.box.x + left.box.w:
            right.score += 1
            print(right.score)
            self.reset()
        elif self.ball.box.x > right.box.x:
            left.score += 1
            print(left.score)
            self.reset()

    def net(self):
        a = 5
        marker = 35
        w = self.window.get_width()
        for y in range(0, self.window.get_height(), 2 * marker):
            pygame.draw.rect(self.window, WHITE, (w // 2 - a, y, 2 * a, marker))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_render(self):
        step = 8
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1.move(self.window, -step)
        elif keys[pygame.K_s]:
            self.player1.move(self.window, step)

        if keys[pygame.K_UP]:
            self.player2.move(self.window, -step)
        elif keys[pygame.K_DOWN]:
            self.player2.move(self.window, step)

        self.window.fill(BLACK)
        self.net()
        self.player1.redraw(self.window)
        self.player2.redraw(self.window)
        self.ball.redraw(self.window)
        self.bounce()
        self.score()


    def run(self):
        timer = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_render()
            pygame.display.update()
            timer.tick(60)
        pygame.quit()


if __name__ == '__main__':
    game = Game('Pong', 800, 480)
    game.run()
