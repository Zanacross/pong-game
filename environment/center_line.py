import pygame

class CenterLine():
    def __init__(self, screen):
        self.rects = []
        self.screen = screen
        self.line_height = 50
        self.line_width = 20
        self.line_gap = 40

    def gen(self):
        totalpadding = self.line_gap + self.line_height + self.line_gap
        total = self.screen.get_height() / (self.line_height + self.line_gap)
        x = self.screen.get_width() / 2
        y = self.line_gap
        for i in range(0, round(total)):
            self.rects.append(Line(x, y, self.line_width, self.line_height))
            y += totalpadding

    def draw(self):
        for i in self.rects:
            pygame.draw.rect(self.screen, i.background, i.rect)



class Line():
    def __init__(self, w, h, x, y):
        self.rect = pygame.Rect((w, h, x, y))
        self.background = pygame.color.Color("white")


