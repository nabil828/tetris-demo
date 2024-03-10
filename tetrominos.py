import pygame
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
