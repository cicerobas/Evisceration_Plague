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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.move(True, "L")
                    if event.key == pygame.K_d:
                        self.player.move(True, "R")
                    if event.key == pygame.K_RETURN:
                        self.player.attack(True)
                    if event.key == pygame.K_r:
                        self.player.is_reload = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.move(False)
                    if event.key == pygame.K_d:
                        self.player.move(False)


            self.window.fill((128,128,128))
            self.player_animation.draw(self.window)
            self.player_animation.update(0.10)

            pygame.display.flip()
            clock.tick(60)
