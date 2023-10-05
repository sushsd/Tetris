import pygame
import time
from grid import Grid
from tetriminoFactory import TetriminoFactory
from score import Scoreboard
from preview import TetriminoPreview


def draw_game_over(screen):
    font = pygame.font.SysFont('Comic Sans MS', 70)
    surface = font.render('Game Over!', True, (255, 255, 255))
    screen.blit(surface, (200, 200))


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((750, 1000))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    running = True

    scoreboard = Scoreboard(screen)
    grid = Grid(screen, scoreboard)
    grid.debug()

    factory = TetriminoFactory(grid)
    tetrimino = factory.produce_tetrimino()
    lastTickTime = time.time()

    preview = TetriminoPreview(screen, factory)
    is_game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    tetrimino.rotate()
                elif event.key == pygame.K_a:
                    tetrimino.move('left')
                elif event.key == pygame.K_d:
                    tetrimino.move('right')
                elif event.key == pygame.K_s:
                    tetrimino.move('down')
                elif event.key == pygame.K_SPACE:
                    tetrimino.drop()

        screen.fill("black")

        if time.time() - lastTickTime >= 1 and not is_game_over:
            if not tetrimino.isActive:
                tetrimino = factory.produce_tetrimino()

                if not tetrimino.hasValidPosition:
                    is_game_over = True
            else:
                tetrimino.move('down')

            lastTickTime = time.time()

        grid.draw()
        scoreboard.draw_scoreboard(510, 700)
        preview.draw(510, 10)

        if is_game_over:
            draw_game_over(screen)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
