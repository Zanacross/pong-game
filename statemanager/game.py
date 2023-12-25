import pygame, random, sys

from paddle.player import Player, Enemy
from ball.ball import Ball
from environment.walls import Walls
from environment.center_line import CenterLine
from ui.score import Score
from pygame.locals import *
class Game():
    def __init__(self, screen, clock):
        self.screen = screen
        self.paused = False
        self.clock = clock
        self.state_end = False
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height()

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
        player_x = self.screen_width / 2 - 200
        enemy_x = self.screen_width / 2 + 200
        self.ui = {
            'player': Score(self.screen, "Player", player_x, 200),
            'enemy': Score(self.screen, "Enemy", enemy_x, 200)
        }
        self.ball = Ball(self.screen)
        self.line = CenterLine(self.screen)
        self.line.gen()

    def start(self):
        self.reset()

    def reset(self):
        for i, k in self.paddles.items():
            k.rect.y = self.screen.get_height() / 2
        for i, k in self.ui.items():
            k.update()
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
        self.line.draw()
        self.paddles['player'].draw()
        self.paddles['enemy'].draw()
        for i, k in self.ui.items():
            k.draw()
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
                elif i == 'left':
                    self.ui['enemy'].score += 1
                    self.ui['enemy'].update()
                    self.reset()
                elif i == 'right':
                    self.ui['player'].score += 1
                    self.reset()
        if self.ui['enemy'].score == 3:
            self.state_end = True
        self.paddles['enemy'].update(self.ball.ball.y)
        self.clock.tick(60)
        pygame.display.flip()