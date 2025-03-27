from code.Entity import Entity


class Zombie(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass

    def attack(self):
        pass
