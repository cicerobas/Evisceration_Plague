from abc import ABC, abstractmethod

from code.Animations import Animations


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.speed = 0
        self.health = 0
        self.damage = 0
        self.animations = Animations(name)
        self.surf = self.animations.get('Idle', False)[0]
        self.rect = self.surf.get_rect(centerx=position[0], bottom=position[1])

    @abstractmethod
    def move(self, direction: str):
        pass

    @abstractmethod
    def attack(self):
        pass
