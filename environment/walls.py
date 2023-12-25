import pygame
class Walls():
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, pygame.color.Color("blue"), self.rect)