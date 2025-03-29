import pygame

from code.Constants import ANIMATION_COOLDOWN, INITIAL_AMMO, WEAPON_CAPACITY
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_options = {
            0: "Idle",
            1: "Walk",
            2: "Run",
            3: "Attack_1",
            4: "Attack_2",
            5: "Shot",
            6: "Reload",
        }
        self.attack_option = 3
        self.reloading = False
        self.shooting = False
        self.running = False
        self.ammo = INITIAL_AMMO
        self.weapon_ammo = WEAPON_CAPACITY

    def update(self):
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.current_frame += 1

        if self.current_frame >= len(self.animation_frames):
            self.current_frame = 0

            if self.shooting or self.reloading:
                self.update_ammo(self.shooting, self.reloading)

            self.attacking = False
            self.reloading = False
            self.shooting = False

        self.image = self.animation_frames[self.current_frame]

    def update_action(self, new_action):
        if new_action != self.action:
            self.running = new_action == 2
            self.action = new_action
            self.animation_frames = self.animations.get_frames(self.animation_options[self.action],
                                                               self.direction == "L")
            self.current_frame = 0
            self.update_time = pygame.time.get_ticks()

    def set_moving(self, is_moving: bool, direction: str = ""):
        if is_moving:
            self.moving = True
            self.direction = direction
        else:
            self.moving = False

    def move(self):
        pass

    def attack(self):
        self.attacking = True
        self.attack_option = 3 if self.attack_option == 4 else 4

    def shot(self):
        self.shooting = True

    def reload(self):
        if self.ammo >= 1 and self.weapon_ammo != WEAPON_CAPACITY:
            self.reloading = True

    def update_ammo(self, shot: bool, reload: bool):
        if shot:
            self.weapon_ammo -= 1
        if reload:
            to_reload = WEAPON_CAPACITY - self.weapon_ammo
            if to_reload <= self.ammo:
                self.ammo -= to_reload
                self.weapon_ammo = WEAPON_CAPACITY
            else:
                self.weapon_ammo = self.ammo
                self.ammo = 0

        # print(f'AMMO {self.weapon_ammo}/{self.ammo}')
