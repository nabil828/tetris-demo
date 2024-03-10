import pygame
from command import Command
from grid import Grid
from tetrominos import (
    ITetromino,
    OTetromino,
    ZTetromino,
    TTetromino,
    STetromino,
    JTetromino,
    LTetromino,
)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (300, 600)
        )  # set the screen size to 300x600 . 20rowsx10columns grid. Each cell is 30x30 pixels

        # game object
        self.grid = Grid()
        self.tetromino = TTetromino()
        # ui object

    def run(self):
        while True:
            command = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        command = Command.LEFT
                    if event.key == pygame.K_RIGHT:
                        command = Command.RIGHT
                    if event.key == pygame.K_DOWN:
                        command = Command.DOWN
                    if event.key == pygame.K_UP:
                        command = Command.UP

            self.update(command)
            self.draw()
            pygame.display.update()

    def draw(self):
        self.grid.draw(self.screen)
        self.tetromino.draw(self.screen)

    def update(self, command):
        self.tetromino.update(command)