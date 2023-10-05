import pygame
from tetriminoFactory import TetriminoFactory
from tetrimino import *


class TetriminoPreview:

    def __init__(self, screen, factory):
        self.screen = screen
        self.factory = factory
        self.textSurface = None
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.textSurface = self.font.render('Next:', True, (255, 255, 255))

    def draw(self, x, y):
        background_square = pygame.Rect(x, y, 230, 290)
        foreground_square = pygame.Rect(x + 10, y + 10, 210, 270)
        background_color = (255, 255, 255)
        pygame.draw.rect(self.screen, background_color, background_square)
        pygame.draw.rect(self.screen, (0, 0, 0), foreground_square)
        self.screen.blit(self.textSurface, (x + 20, y + 20))

        if self.factory.nextNumber == 0:
            ITetrimino.draw_preview(self.screen, x + 85, y + 60)
        elif self.factory.nextNumber == 1:
            OTetrimino.draw_preview(self.screen, x + 85, y + 60)
        elif self.factory.nextNumber == 2:
            TTetrimino.draw_preview(self.screen, x + 85, y + 60)
        elif self.factory.nextNumber == 3:
            LTetrimino.draw_preview(self.screen, x + 85, y + 60)
        elif self.factory.nextNumber == 4:
            STetrimino.draw_preview(self.screen, x + 85, y + 60)
