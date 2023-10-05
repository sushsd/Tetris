from grid import Field, add
import pygame
import copy


class Tetrimino:
    def __init__(self, field1, field2, field3, field4, position, grid, color_index):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
        self.position = position
        self.orientation = 0
        self.grid = grid
        self.isActive = True
        self.hasValidPosition = True
        self.colorIndex = color_index

        if not self.check_if_valid_position(self.field1, self.field2, self.field3, self.field4):
            self.hasValidPosition = False

        grid.set_fields(self.map_to_grid(), self.colorIndex)

    def map_to_grid(self):
        return [add(self.field1, self.position),
                add(self.field2, self.position),
                add(self.field3, self.position),
                add(self.field4, self.position)]

    def map_to_grid_position(self, position):
        return [add(self.field1, position),
                add(self.field2, position),
                add(self.field3, position),
                add(self.field4, position)]

    def map_to_grid_fields(self, field1, field2, field3, field4):
        return [add(field1, self.position),
                add(field2, self.position),
                add(field3, self.position),
                add(field4, self.position)]

    def rotate(self):
        pass

    def detect_collision_move(self, direction):
        new_position = copy.copy(self.position)

        if direction == 'down':
            new_position.y += 1
        elif direction == 'left':
            new_position.x -= 1
        elif direction == 'right':
            new_position.x += 1

        grid_positions = self.map_to_grid_position(new_position)
        can_move = True

        for position in grid_positions:
            if position.y > 19:
                can_move = False
                break
            if position.x < 0:
                can_move = False
                break
            if position.x > 9:
                can_move = False
                break
            if self.grid.get_field(position.x, position.y) != 0:
                can_move = False
                break

        return can_move

    def detect_collision_rotate(self):
        pass

    def check_if_valid_position(self, field1, field2, field3, field4):
        grid_positions = self.map_to_grid_fields(field1, field2, field3, field4)
        can_rotate = True

        for position in grid_positions:
            if position.y > 19:
                can_rotate = False
                break
            if position.x < 0:
                can_rotate = False
                break
            if position.x > 9:
                can_rotate = False
                break
            if self.grid.get_field(position.x, position.y) != 0:
                can_rotate = False
                break

        return can_rotate

    def move(self, direction):
        self.grid.set_fields(self.map_to_grid(), 0)

        can_move = self.detect_collision_move(direction)

        if direction == 'down':
            if can_move:
                self.position.y += 1
        elif direction == 'left':
            if can_move:
                self.position.x -= 1
        elif direction == 'right':
            if can_move:
                self.position.x += 1

        self.grid.set_fields(self.map_to_grid(), self.colorIndex)

        if direction == 'down' and not can_move:
            self.isActive = False
            self.grid.after_block_placed()
            return False
        else:
            return True

    def drop(self):
        can_move = True
        while can_move:
            can_move = self.move('down')


class ITetrimino(Tetrimino):
    def __init__(self, grid):
        super().__init__(Field(0, 0), Field(0, 1), Field(0, 2), Field(0, 3), Field(4, 0), grid, 1)

    def rotate(self):
        self.grid.set_fields(self.map_to_grid(), 0)
        can_rotate = self.detect_collision_rotate()
        if can_rotate:
            if self.orientation == 0:
                self.field1 = Field(0, 0)
                self.field2 = Field(1, 0)
                self.field3 = Field(2, 0)
                self.field4 = Field(3, 0)
                self.orientation = 90
            elif self.orientation == 90:
                self.field1 = Field(0, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(0, 2)
                self.field4 = Field(0, 3)
                self.orientation = 0
        self.grid.set_fields(self.map_to_grid(), self.colorIndex)

    def detect_collision_rotate(self):

        new_field1 = copy.copy(self.field1)
        new_field2 = copy.copy(self.field2)
        new_field3 = copy.copy(self.field3)
        new_field4 = copy.copy(self.field4)

        if self.orientation == 0:
            new_field1 = Field(0, 0)
            new_field2 = Field(1, 0)
            new_field3 = Field(2, 0)
            new_field4 = Field(3, 0)
        elif self.orientation == 90:
            new_field1 = Field(0, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(0, 2)
            new_field4 = Field(0, 3)

        return self.check_if_valid_position(new_field1, new_field2, new_field3, new_field4)

    @staticmethod
    def draw_preview(screen, x, y):
        color = (51, 255, 255)  # blue

        square1 = pygame.Rect(x, y, 40, 40)
        square2 = pygame.Rect(x, y + 50, 40, 40)
        square3 = pygame.Rect(x, y + 100, 40, 40)
        square4 = pygame.Rect(x, y + 150, 40, 40)

        pygame.draw.rect(screen, color, square1)
        pygame.draw.rect(screen, color, square2)
        pygame.draw.rect(screen, color, square3)
        pygame.draw.rect(screen, color, square4)


class OTetrimino(Tetrimino):
    def __init__(self, grid):
        super().__init__(Field(0, 0), Field(0, 1), Field(1, 0), Field(1, 1), Field(4, 0), grid, 2)

    @staticmethod
    def draw_preview(screen, x, y):
        color = (255, 255, 0)  # yellow

        square1 = pygame.Rect(x, y, 40, 40)
        square2 = pygame.Rect(x, y + 50, 40, 40)
        square3 = pygame.Rect(x + 50, y, 40, 40)
        square4 = pygame.Rect(x + 50, y + 50, 40, 40)

        pygame.draw.rect(screen, color, square1)
        pygame.draw.rect(screen, color, square2)
        pygame.draw.rect(screen, color, square3)
        pygame.draw.rect(screen, color, square4)


class TTetrimino(Tetrimino):
    def __init__(self, grid):
        super().__init__(Field(0, 0), Field(1, 0), Field(2, 0), Field(1, 1), Field(4, 0), grid, 3)

    def rotate(self):
        self.grid.set_fields(self.map_to_grid(), 0)
        can_rotate = self.detect_collision_rotate()
        if can_rotate:
            if self.orientation == 0:
                self.field1 = Field(1, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(1, 1)
                self.field4 = Field(1, 2)
                self.orientation = 90
            elif self.orientation == 90:
                self.field1 = Field(1, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(1, 1)
                self.field4 = Field(2, 1)
                self.orientation = 180
            elif self.orientation == 180:
                self.field1 = Field(0, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(0, 2)
                self.field4 = Field(1, 1)
                self.orientation = 270
            elif self.orientation == 270:
                self.field1 = Field(0, 0)
                self.field2 = Field(1, 0)
                self.field3 = Field(2, 0)
                self.field4 = Field(1, 1)
                self.orientation = 0
        self.grid.set_fields(self.map_to_grid(), self.colorIndex)

    def detect_collision_rotate(self):
        new_field1 = copy.copy(self.field1)
        new_field2 = copy.copy(self.field2)
        new_field3 = copy.copy(self.field3)
        new_field4 = copy.copy(self.field4)

        if self.orientation == 0:
            new_field1 = Field(1, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(1, 1)
            new_field4 = Field(1, 2)

        elif self.orientation == 90:
            new_field1 = Field(1, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(1, 1)
            new_field4 = Field(2, 1)

        elif self.orientation == 180:
            new_field1 = Field(0, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(0, 2)
            new_field4 = Field(1, 1)

        elif self.orientation == 270:
            new_field1 = Field(0, 0)
            new_field2 = Field(1, 0)
            new_field3 = Field(2, 0)
            new_field4 = Field(1, 1)

        return self.check_if_valid_position(new_field1, new_field2, new_field3, new_field4)

    @staticmethod
    def draw_preview(screen, x, y):
        color = (255, 0, 255)  # pink

        square1 = pygame.Rect(x, y, 40, 40)
        square2 = pygame.Rect(x + 50, y, 40, 40)
        square3 = pygame.Rect(x + 100, y, 40, 40)
        square4 = pygame.Rect(x + 50, y + 50, 40, 40)

        pygame.draw.rect(screen, color, square1)
        pygame.draw.rect(screen, color, square2)
        pygame.draw.rect(screen, color, square3)
        pygame.draw.rect(screen, color, square4)


class LTetrimino(Tetrimino):
    def __init__(self, grid):
        super().__init__(Field(0, 0), Field(0, 1), Field(0, 2), Field(1, 2), Field(4, 0), grid, 4)

    def rotate(self):
        self.grid.set_fields(self.map_to_grid(), 0)
        can_rotate = self.detect_collision_rotate()
        if can_rotate:
            if self.orientation == 0:
                self.field1 = Field(0, 0)
                self.field2 = Field(1, 0)
                self.field3 = Field(2, 0)
                self.field4 = Field(0, 1)
                self.orientation = 90
            elif self.orientation == 90:
                self.field1 = Field(0, 0)
                self.field2 = Field(1, 0)
                self.field3 = Field(1, 1)
                self.field4 = Field(1, 2)
                self.orientation = 180
            elif self.orientation == 180:
                self.field1 = Field(0, 1)
                self.field2 = Field(1, 1)
                self.field3 = Field(2, 1)
                self.field4 = Field(2, 0)
                self.orientation = 270
            elif self.orientation == 270:
                self.field1 = Field(0, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(0, 2)
                self.field4 = Field(1, 2)
                self.orientation = 0
        self.grid.set_fields(self.map_to_grid(), self.colorIndex)

    def detect_collision_rotate(self):
        new_field1 = copy.copy(self.field1)
        new_field2 = copy.copy(self.field2)
        new_field3 = copy.copy(self.field3)
        new_field4 = copy.copy(self.field4)

        if self.orientation == 0:
            new_field1 = Field(0, 0)
            new_field2 = Field(1, 0)
            new_field3 = Field(2, 0)
            new_field4 = Field(0, 1)

        elif self.orientation == 90:
            new_field1 = Field(0, 0)
            new_field2 = Field(1, 0)
            new_field3 = Field(1, 1)
            new_field4 = Field(1, 2)

        elif self.orientation == 180:
            new_field1 = Field(0, 1)
            new_field2 = Field(1, 1)
            new_field3 = Field(2, 1)
            new_field4 = Field(2, 0)

        elif self.orientation == 270:
            new_field1 = Field(0, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(0, 2)
            new_field4 = Field(1, 2)

        return self.check_if_valid_position(new_field1, new_field2, new_field3, new_field4)

    @staticmethod
    def draw_preview(screen, x, y):
        color = (255, 128, 0)  # orange

        square1 = pygame.Rect(x, y, 40, 40)
        square2 = pygame.Rect(x, y + 50, 40, 40)
        square3 = pygame.Rect(x, y + 100, 40, 40)
        square4 = pygame.Rect(x + 50, y + 100, 40, 40)

        pygame.draw.rect(screen, color, square1)
        pygame.draw.rect(screen, color, square2)
        pygame.draw.rect(screen, color, square3)
        pygame.draw.rect(screen, color, square4)


class STetrimino(Tetrimino):
    def __init__(self, grid):
        super().__init__(Field(0, 1), Field(1, 1), Field(1, 0), Field(2, 0), Field(4, 0), grid, 5)

    def rotate(self):
        self.grid.set_fields(self.map_to_grid(), 0)
        can_rotate = self.detect_collision_rotate()
        if can_rotate:
            if self.orientation == 0:
                self.field1 = Field(0, 0)
                self.field2 = Field(0, 1)
                self.field3 = Field(1, 1)
                self.field4 = Field(1, 2)
                self.orientation = 90
            elif self.orientation == 90:
                self.field1 = Field(0, 1)
                self.field2 = Field(1, 1)
                self.field3 = Field(1, 0)
                self.field4 = Field(2, 0)
                self.orientation = 0
        self.grid.set_fields(self.map_to_grid(), self.colorIndex)

    def detect_collision_rotate(self):

        new_field1 = copy.copy(self.field1)
        new_field2 = copy.copy(self.field2)
        new_field3 = copy.copy(self.field3)
        new_field4 = copy.copy(self.field4)

        if self.orientation == 0:
            new_field1 = Field(0, 0)
            new_field2 = Field(0, 1)
            new_field3 = Field(1, 1)
            new_field4 = Field(1, 2)
        elif self.orientation == 90:
            new_field1 = Field(0, 1)
            new_field2 = Field(1, 1)
            new_field3 = Field(1, 0)
            new_field4 = Field(2, 0)

        return self.check_if_valid_position(new_field1, new_field2, new_field3, new_field4)

    @staticmethod
    def draw_preview(screen, x, y):
        color = (0, 255, 0)  # green

        square1 = pygame.Rect(x, y + 50, 40, 40)
        square2 = pygame.Rect(x + 50, y + 50, 40, 40)
        square3 = pygame.Rect(x + 50, y, 40, 40)
        square4 = pygame.Rect(x + 100, y, 40, 40)

        pygame.draw.rect(screen, color, square1)
        pygame.draw.rect(screen, color, square2)
        pygame.draw.rect(screen, color, square3)
        pygame.draw.rect(screen, color, square4)
