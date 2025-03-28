import pygame
from pygame import Surface

from code.Constants import WIN_WIDTH, WIN_HEIGHT
from code.EntityFactory import EntityFactory


class World:
    def __init__(self, window: Surface):
        self.window = window
        self.scroll = 0

        self.bg_images = []
        self.road_image = pygame.image.load("./assets/sprites/World/Road.png")
        for i in range(0, 5):
            image = pygame.image.load(f"./assets/sprites/World/World_BG_{i}.png").convert_alpha()
            self.bg_images.append(image)

        self.entity_list = []
        self.player = EntityFactory.get_entity("Player")
        self.entity_list.append(self.player)

    def draw_bg(self):
        for i, img in enumerate(self.bg_images):
            speed = self.player.speed * 10 + (i * 0.3)
            pos_x = (self.scroll * speed) % WIN_WIDTH
            self.window.blit(img, (-pos_x, 0))
            self.window.blit(img, (-pos_x + WIN_WIDTH, 0))

    def draw_road(self):
        speed = 1 + self.player.speed * 10
        pos_x = (self.scroll * speed) % WIN_WIDTH
        self.window.blit(self.road_image, (-pos_x, 0))
        self.window.blit(self.road_image, (-pos_x + WIN_WIDTH, 0))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(60)
            self.draw_bg()
            self.draw_road()

            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)
                entity.update_animation()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.player.move("R")
                self.scroll += self.player.speed * 5
            if keys[pygame.K_LEFT]:
                self.player.move("L")
                self.scroll -= self.player.speed * 5

            # TODO Corrigir BUG, pressionando SETA+ATAQUE, trava o personagem na animação de caminhada
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.attack()
                if event.type == pygame.KEYUP:
                    if not self.player.attacking:
                        self.player.current_animation = "Idle"

            pygame.display.flip()
