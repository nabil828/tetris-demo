import pygame
from command import Command
from resources.colors import Colors


class Tetromino:
    def __init__(self) -> None:
        self.state = 0
        self.col_offset = 4
        self.row_offset = 0

    def draw(self, screen):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30,
                            (row_index + self.row_offset) * 30,
                            30 - 1,
                            30 - 1,
                        ),
                    )
    
    def update(self, command: Command, game):
        if command == Command.LEFT:
            self.move_left(game)
        if command == Command.RIGHT:
            self.move_right(game)
        if command == Command.DOWN:
            self.move_down(game)
        if command == Command.UP:
            self.rotate()

    def move_left(self, game):
        self.col_offset -= 1
        if(self.out_of_bounds()):
            self.col_offset += 1
        
        if (self.collides_with_other_tetrominos(game)):
            self.col_offset += 1

    def move_right(self, game):
        self.col_offset += 1
        if(self.out_of_bounds()):
            self.col_offset -= 1

        if (self.collides_with_other_tetrominos(game)):
            self.col_offset -= 1

    def move_down(self, game):
        self.row_offset += 1
        if(self.out_of_bounds()):
            self.row_offset -= 1
            self.lock_tetromino(game)
            game.spawn_new_tetromino()
            return
        
        if (self.collides_with_other_tetrominos(game)):
            self.row_offset -= 1
            self.lock_tetromino(game)
            game.spawn_new_tetromino()
            return


    

    def out_of_bounds(self):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    if (
                        col_index + self.col_offset < 0
                        or col_index + self.col_offset > 9
                        or row_index + self.row_offset > 19
                    ):
                        return True
        return False
    
    def rotate(self):
        self.state = (self.state + 1) % len(self.blocks)
        if(self.out_of_bounds()):
            self.state = (self.state - 1 ) % len(self.blocks)

    def lock_tetromino(self, game):
        """
        Carbon copy the tetromino into the grid
        """
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    game.grid.blocks[row_index + self.row_offset][col_index + self.col_offset] = self.color
    
    def collides_with_other_tetrominos(self, game):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    if row_index + self.row_offset <= 19:
                        if game.grid.blocks[row_index + self.row_offset][col_index + self.col_offset]:
                            return True
        return False



class ZTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.BLUE.value
        self.blocks = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0],
            ],
        ]


class OTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.YELLOW.value
        self.blocks = [
            [
                [1, 1],
                [1, 1],
            ]
        ]


class ITetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.ORANGE.value
        self.blocks = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
            ],
        ]
        self.col_offset = 3
        self.row_offset = -1


class STetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.PURPLE.value
        self.blocks = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0],
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class JTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.RED.value
        self.blocks = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0],
            ],
        ]


class LTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.GREEN.value
        self.blocks = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0],
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0],
            ],
        ]


class TTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.CYAN.value
        self.blocks = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]
