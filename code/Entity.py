from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from code.Animations import Animations


class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__()
        self.name = name
        self.speed = 0
        self.health = 0
        self.damage = 0
        self.animations = Animations(name)
        self.animation_frames: list[Surface] = self.animations.get_frames('Idle', False)
        self.current_frame = 0
        self.moving = False
        self.attacking = False
        self.direction = "R"
        self.image = self.animation_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass
