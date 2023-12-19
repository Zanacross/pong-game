import pygame, sys, os, random

from pygame.locals import *
pygame.init()
pygame.key.set_repeat(10)


class game():
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.paused = False
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height()
        pygame.display.set_caption("Pong Game")
        self.paddles = {
            "player": Player(self.screen),
            "enemy": Enemy(self.screen)
        }
        self.walls = {
            "left": Walls(self.screen, Rect((10, 10, 1, self.screen_height))),
            "right": Walls(self.screen, Rect((self.screen_width-10, 10, 1, self.screen_height))),
            "top": Walls(self.screen, Rect((0, 0, self.screen_width, 10))),
            "bottom": Walls(self.screen, Rect((0, self.screen_height - 10, self.screen_width, 10)))
        }
        self.ui = {
            'score': Score(self.screen)
        }
        self.ball = Ball(self.screen)



    def start(self):
        self.reset()

    def reset(self):
        for i, k in self.paddles.items():
            k.rect.y = self.screen.get_height() / 2
        self.ball.reset()
        self.ball.direction['x'] = random.randint(0,1)
        self.ball.direction['y'] = random.randint(0,1)

    def event(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_p or e.key == K_ESCAPE:
                    if not self.paused:
                        self.paused = True
                    else:
                        self.paused = False
            self.paddles['player'].event(e)


    def draw(self):
        self.screen.fill(pygame.color.Color("black"))
        self.paddles['player'].draw()
        self.paddles['enemy'].draw()
        for i, k in self.walls.items():
            k.draw()
        self.ball.draw()

    def update(self):
        self.ball.update()
        for i, k in self.paddles.items():
            if self.ball.check_collision(k.rect):
                if i == 'player':
                    self.ball.direction['x'] = 0
                else:
                    self.ball.direction['x'] = 1
        for i, k in self.walls.items():
            if self.ball.check_collision(k.rect):
                if i in ['top', 'bottom']:
                    if i == 'top':
                        self.ball.direction['y'] = 0
                    else:
                        self.ball.direction['y'] = 1
                else:
                    self.reset()
        self.paddles['enemy'].update(self.ball.ball.y)
        self.clock.tick(60)
        pygame.display.flip()


class Paddle():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    def draw(self):
        pass

    def update(self, *args):
        pass

    def event(self, e):
        pass

class Player(Paddle):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect = pygame.Rect(100, 100, 20 ,120)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("white"), self.rect)

    def event(self, e):
        if e.type == KEYDOWN:
            if e.key == K_w:
                self.rect.y -= 10
            if e.key == K_s:
                self.rect.y += 10

class Enemy(Paddle):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect = pygame.Rect(self.screen.get_width() - 100, 100, 20, 120)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("white"), self.rect)

    def update(self, ball_pos):
        ball_pos = ball_pos
        if ball_pos >= self.rect.y:
            self.rect.y += 10
        else:
            self.rect.y -= 10


class Ball():
    def __init__(self, screen):
        self.screen = screen
        self.center_x, self.center_y = self.screen.get_width() / 2, self.screen.get_height() / 2
        self.ball = pygame.Rect((self.center_x, self.center_y, 25, 25))
        self.direction = {
            'x': 0,
            'y': 0
        }
        self.speed = 10
    def draw(self):
        pygame.draw.rect(self.screen, "red", self.ball, 100, 100)

    def update(self):
        print(self.direction['x'])
        if self.direction['x'] == 0:
            self.ball.x += self.speed
        if self.direction['x'] == 1:
            self.ball.x -= self.speed
        if self.direction['y'] == 0:
            self.ball.y += self.speed
        if self.direction['y'] == 1:
            self.ball.y -= self.speed

    def check_collision(self, point):
        if self.ball.colliderect(point):
            print("hit")
            return True

    def reset(self):
        self.ball = pygame.Rect((self.center_x, self.center_y, 25, 25))

class Walls():
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("blue"), self.rect)

class Score():
    def __init__(self, screen):
        self.screen = screen
        self.scores = {
            'player': 0,
            'enemy': 0
        }

    def add_score(self, player):
        self.scores[player] += 1
g = game()
g.start()
while g.running:
    g.event()
    if not g.paused:
        g.draw()
        g.update()
