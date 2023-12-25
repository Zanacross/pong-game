import pygame, sys, os, random

from pygame.locals import *
from statemanager.state_manager import State_Manager

pygame.init()
pygame.key.set_repeat(10)


class game():
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.paused = False
        pygame.display.set_caption("Pong Game")

        self.state_manager = State_Manager(self.screen, self.clock)

    def update(self):
        self.state_manager.current.update()
        if self.state_manager.current.state_end:
            self.state_manager.current = self.state_manager.states['game_over']

    def draw(self):
        self.state_manager.current.draw()

    def event(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
        self.state_manager.current.event()



g = game()
g.state_manager.current.start()
while g.running:
    g.event()
    if not g.state_manager.current.paused:
        g.draw()
        g.update()
