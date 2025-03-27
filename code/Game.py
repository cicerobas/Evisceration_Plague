import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((960, 540))

    def run(self):
        running = True

        while running:
            menu = Menu(self.window)
            menu.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
