import pygame


def add(lhs, rhs):
    add_x = lhs.x + rhs.x
    add_y = lhs.y + rhs.y
    result = Field(add_x, add_y)
    return result


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_color_for_field(number):
    if number == 0:
        return (105, 105, 105)  # grey
    elif number == 1:
        return (51, 255, 255)  # blue
    elif number == 2:
        return (255, 255, 0)  # yellow
    elif number == 3:
        return (255, 0, 255)  # pink
    elif number == 4:
        return (255, 128, 0)  # orange
    elif number == 5:
        return (0, 255, 0)  # green


class Grid:
    def __init__(self, screen, scoreboard):
        self.scoreboard = scoreboard
        self.grid = []
        for x in range(10):
            column = []
            for y in range(20):
                column.append(0)
            self.grid.append(column)
        self.screen = screen

    def debug(self):
        print(self.grid)

    def get_field(self, x, y):
        return self.grid[x][y]

    def after_block_placed(self):
        number_of_full_lines = 0
        for y in range(20):
            is_row_full = True
            for x in range(10):
                if self.grid[x][y] == 0:
                    is_row_full = False
                    break
            if is_row_full:
                number_of_full_lines += 1
                for x in range(10):
                    self.grid[x].pop(y)
                    self.grid[x].insert(0, 0)

        self.scoreboard.score_lines(number_of_full_lines)

    def draw(self):
        for x in range(10):
            for y in range(20):
                square = pygame.Rect(5 + x * 50, 5 + y * 50, 40, 40)
                color = get_color_for_field(self.grid[x][y])
                pygame.draw.rect(self.screen, color, square)

    def set_fields(self, fields, value):
        for place in fields:
            self.grid[place.x][place.y] = value
