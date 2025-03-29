import pygame
from pygame import Surface

from code.Constants import WIN_WIDTH
from code.EntityFactory import EntityFactory


class World:
    def __init__(self, window: Surface):
        self.window = window

        self.player_animation = pygame.sprite.GroupSingle()
        self.player = EntityFactory.get_entity("Player")
        self.player_animation.add(self.player)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            if self.player.shooting:
                self.player.update_action(5)
            elif self.player.reloading:
                self.player.update_action(6)
            elif self.player.attacking:
                self.player.update_action(self.player.attack_option)
            elif self.player.moving:
                self.player.update_action(1)
            else:
                self.player.update_action(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.set_moving(True, "L")
                    if event.key == pygame.K_d:
                        self.player.set_moving(True, "R")
                    if event.key == pygame.K_q:
                        self.player.attack()
                    if event.key == pygame.K_r:
                        self.player.reload()
                    if event.key == pygame.K_SPACE:
                        if self.player.weapon_ammo >= 1:
                            self.player.shot()
                        else:
                            self.player.reload()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.set_moving(False)
                    if event.key == pygame.K_d:
                        self.player.set_moving(False)

            self.window.fill((128, 128, 128))
            self.player_animation.draw(self.window)
            self.player_animation.update()

            pygame.display.update()
            clock.tick(60)
