import pygame

from code.Constants import WIN_WIDTH, WIN_HEIGHT


class Background:
    def __init__(self, name:str, position:tuple, speed:float):
        self.name = name
        self.speed = speed
        self.surf = pygame.image.load(f"./assets/sprites/World/{self.name}.png").convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH