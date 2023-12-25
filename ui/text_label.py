import pygame, os

class Text_label():
    def __init__(self, screen, text, x, y, font_name, font_size, color):
        self.screen = screen
        self.text = text

        self.pos = {
            'x': x,
            'y': y
        }
        self.font_name = font_name
        self.font_size = font_size
        self.color = color
        if self.font_name in pygame.font.get_fonts():
            self.font = pygame.font.SysFont(self.font_name, self.font_size)
        else:
            self.font = pygame.font.Font(os.path.join("ui/fonts", self.font_name), self.font_size)
        self.render = self.font.render(str(text), 1, (color))

    def set_text(self, new):
        self.text = new
        self.render = self.font.render(str(self.text), 1, (self.color))
