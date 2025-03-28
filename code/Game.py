import pygame

from code.Constants import MENU_OPTIONS, WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.World import World


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        running = True

        while running:
            menu = Menu(self.window)
            menu_option = menu.run()

            if menu_option == MENU_OPTIONS[0]:
                world = World(self.window)
                world.run()

            if menu_option == MENU_OPTIONS[1]:
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
