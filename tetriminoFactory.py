from tetrimino import *
import random


class TetriminoFactory:
    def __init__(self, grid):
        self.grid = grid
        self.nextNumber = random.randint(0, 4)

    def produce_tetrimino(self):

        tetrimino = None

        if self.nextNumber == 0:
            tetrimino = ITetrimino(self.grid)
        elif self.nextNumber == 1:
            tetrimino = OTetrimino(self.grid)
        elif self.nextNumber == 2:
            tetrimino = TTetrimino(self.grid)
        elif self.nextNumber == 3:
            tetrimino = LTetrimino(self.grid)
        elif self.nextNumber == 4:
            tetrimino = STetrimino(self.grid)

        self.nextNumber = random.randint(0, 4)

        return tetrimino
