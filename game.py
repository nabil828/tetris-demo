import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (300, 600)
        )  # set the screen size to 300x600 . 20rowsx10columns grid. Each cell is 30x30 pixels

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("left")
                    if event.key == pygame.K_RIGHT:
                        print("right")
                    if event.key == pygame.K_DOWN:
                        print("down")
                    if event.key == pygame.K_UP:
                        print("up")
            self.draw()
            pygame.display.update()

    def draw(self):
        pass