import pygame


class Grid:
    def __init__(self) -> None:
        self.blocks = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # [[0 for _ in range(10)] for _ in range(20)]

    def draw(self, screen, ui_x_offset, ui_y_offset):
        # screen.fill((100, 100, 100))
        for row_index, row in enumerate(self.blocks):
            for col_index, block in enumerate(row):
                pygame.draw.rect(
                    screen,
                    block,
                    (
                        col_index * 30 + ui_x_offset,
                        row_index * 30 + ui_y_offset,
                        30 - 1,
                        30 - 1,
                    ),
                )

    def check_for_any_full_lines_to_clear(self):
        cleared_lines = 0
        for row_index, row in enumerate(self.blocks):
            if all(row):
                self.blocks.pop(row_index)
                self.blocks.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                cleared_lines += 1
        return cleared_lines
