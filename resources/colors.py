from enum import Enum


class Colors(Enum):
    # add Tetris classic colors
    CYAN = (0, 255, 255) # I
    BLUE = (0, 0, 255) # J
    ORANGE = (255, 165, 0) # L
    YELLOW = (255, 255, 0) # O
    GREEN = (0, 255, 0) # S
    PURPLE = (128, 0, 128) # T
    RED = (255, 0, 0) # Z

    # add Tetris darkened colors
    CYAN_Dark = (0, 180, 180) # I
    BLUE_Dark = (0, 0, 180) # J
    ORANGE_Dark = (255, 165, 0) # L
    YELLOW_Dark = (200, 120, 0) # O
    GREEN_Dark = (0, 180, 0) # S
    PURPLE_Dark = (128, 0, 128) # T
    RED_Dark = (100, 0, 100) # Z

    LIGHT_BLUE = (173, 216, 230)

    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    DARK_BLUE = (0, 0, 128)
    GREY = (100, 100, 100)
    LIGHT_GREY = (192, 192, 192)
    DARK_GREY = (64, 64, 64)
    PINK = (255, 192, 203)
    BROWN = (165, 42, 42)
    LIME = (0, 255, 0)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)
    BACK_BLUE = (146, 168, 209)
    FRONT_BLUE = 3, 79, 132
