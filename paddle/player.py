import random

from paddle.paddle import Paddle
import pygame
from pygame.locals import *

class Player(Paddle):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect = pygame.Rect(100, 100, 20 ,120)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("white"), self.rect)

    def event(self, e):
        if e.type == KEYDOWN:
            if e.key == K_w and self.rect.y > 0:
                self.rect.y -= 10
            if e.key == K_s and self.rect.y < self.screen.get_height() - self.rect.height:
                self.rect.y += 10


class Enemy(Paddle):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect = pygame.Rect(self.screen.get_width() - 100, 100, 20, 120)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("white"), self.rect)

    def update(self, ball_pos):
        ball_pos = ball_pos
        if ball_pos <= self.screen.get_width() / 2:
            if ball_pos >= self.rect.y:
                self.rect.y += random.randint(5,15)
            else:
                self.rect.y -= random.randint(5,15)