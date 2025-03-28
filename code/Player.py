import pygame.key

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.current_animation = "Idle"
        self.current_frame = 0
        self.speed = 0.1
        self.direction = "R"
        self.moving = False
        self.attacking = False
        self.attack_cycle = 1

    def update_animation(self):
        animation = self.animations.get(self.current_animation, self.direction == "L")
        self.current_frame += self.speed
        if int(self.current_frame) >= len(animation):
            self.current_frame = 0
            if self.current_animation in ["Attack_1", "Attack_2"]:
                self.attacking = False
                self.current_animation = "Idle"

        self.surf = animation[int(self.current_frame)]

    def move(self, direction:str):
        self.current_animation = "Walk"
        self.direction = direction
        self.moving = True

    def attack(self):
        if not self.attacking:
            self.moving = False
            self.attacking = True

            if self.attack_cycle == 1:
                self.current_animation = "Attack_1"
                self.attack_cycle = 2
            else:
                self.current_animation = "Attack_2"
                self.attack_cycle = 1

            self.current_frame = 0

