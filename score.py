import pygame


class Scoreboard:
    def __init__(self, screen):
        self.linesSurface = None
        self.scoreSurface = None
        self.score = 0
        self.lines = 0
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.set_score_lines()

    def score_lines(self, number_of_lines):
        if number_of_lines == 4:
            self.score += 800
        else:
            self.score += number_of_lines * 100

        self.lines += number_of_lines
        self.set_score_lines()

    def set_score_lines(self):
        self.scoreSurface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.linesSurface = self.font.render(f'Lines: {self.lines}', True, (255, 255, 255))

    def draw_scoreboard(self, x, y):
        background_square = pygame.Rect(x, y, 230, 290)
        foreground_square = pygame.Rect(x + 10, y + 10, 210, 270)
        background_color = (255, 255, 255)
        pygame.draw.rect(self.screen, background_color, background_square)
        pygame.draw.rect(self.screen, (0, 0, 0), foreground_square)
        self.screen.blit(self.scoreSurface, (x + 20, y + 20))
        self.screen.blit(self.linesSurface, (x + 20, y + 50))
