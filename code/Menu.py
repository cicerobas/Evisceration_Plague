import pygame
from pygame import Surface

from code.Constants import WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        bg = pygame.image.load("./assets/MenuBG.png")
        self.surf = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self):
        self.window.blit(self.surf, self.rect)
        pygame.display.flip()