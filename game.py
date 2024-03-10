import random
import pygame
from command import Command
from grid import Grid
from resources.ui import UI
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
            (500, 620)
        )  # set the screen size to 300x600 . 20rowsx10columns grid. Each cell is 30x30 pixels
        self.game_over = False
        self.score = 0

        # game objects
        self.grid = Grid()
        self.tetromino = self.spawn_new_tetromino()
        self.ui = UI()
        self.next_tetromino = self.spawn_new_tetromino()

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
                        self.update_score(0, 1)
                    if event.key == pygame.K_UP and self.game_over == False:
                        command = Command.UP
                elif event.type == event_every_200ms and self.game_over == False:
                    command = Command.DOWN

            self.update(command)
            self.draw()
            pygame.display.update()

    def draw(self):
        self.ui.draw(self.screen, self)
        self.grid.draw(self.screen, 10, 10)
        self.tetromino.draw(self.screen, 10, 10)

    def update(self, command):
        self.tetromino.update(command, self)

    def spawn_new_tetromino(self):
        return random.choice(
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
        return self.grid.check_for_any_full_lines_to_clear()

    def update_score(self, lined_cleared, move_down_points):
        self.score += move_down_points
        if lined_cleared == 1:
            self.score += 100
        if lined_cleared == 2:
            self.score += 300
        if lined_cleared == 3:
            self.score += 500
