import random
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
        self.game_over = False

        # game object
        self.grid = Grid()
        self.tetromino = TTetromino()
        # ui object

    def run(self):

        event_every_200ms = pygame.USEREVENT + 1
        pygame.time.set_timer(event_every_200ms, 200)

        while True:
            command = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_over == True:
                        self.__init__()
                    if event.key == pygame.K_LEFT and self.game_over == False:
                        command = Command.LEFT
                    if event.key == pygame.K_RIGHT and self.game_over == False:
                        command = Command.RIGHT
                    if event.key == pygame.K_DOWN and self.game_over == False:
                        command = Command.DOWN
                    if event.key == pygame.K_UP and self.game_over == False:
                        command = Command.UP
                elif event.type == event_every_200ms and self.game_over == False:
                    command = Command.DOWN

            self.update(command)
            self.draw()
            pygame.display.update()

    def draw(self):
        self.grid.draw(self.screen)
        self.tetromino.draw(self.screen)

    def update(self, command):
        self.tetromino.update(command, self)

    def spawn_new_tetromino(self):
        self.tetromino = random.choice(
            [
                TTetromino(),
                ITetromino(),
                OTetromino(),
                ZTetromino(),
                STetromino(),
                JTetromino(),
                LTetromino(),
            ]
        )

    def check_for_any_full_lines_to_clear(self):
        self.grid.check_for_any_full_lines_to_clear()
