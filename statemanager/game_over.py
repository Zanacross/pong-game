from ui.text_label import Text_label
import pygame

class Game_Over():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.paused = False
        self.state_end = False
        self.w, self.h = self.screen.get_width() / 2, self.screen.get_height() / 2
        self.label = Text_label(self.screen, "Big Old Game Over", self.w, self.h,"Symtext.ttf", 50, "red")

    def draw(self):
        self.screen.fill(pygame.color.Color("black"))
        self.screen.blit(self.label.render, (self.w - self.label.render.get_width() /2, self.h))
    def update(self):
        self.clock.tick(60)
        pygame.display.flip()
    def event(self):
        pass