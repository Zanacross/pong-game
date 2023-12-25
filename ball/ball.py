import pygame

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
            return True

    def reset(self):
        self.ball = pygame.Rect((self.center_x, self.center_y, 25, 25))