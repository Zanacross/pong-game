from ui.text_label import Text_label


class Score:
    def __init__(self, screen, score_text, x, y):
        self.score_name = score_text
        self.score = 0
        self.screen = screen
        self.score_text = self.score_name + ": " + str(self.score)

        self.x, self.y = x, y
        self.label = Text_label(self.screen, self.score_text, x, y, "Symtext.ttf", 25, "red")

    def draw(self):
        self.screen.blit(self.label.render, (self.x, self.y))

    def update(self):
        self.score_text = self.score_name + ": " + str(self.score)
        self.label.set_text(self.score_text)