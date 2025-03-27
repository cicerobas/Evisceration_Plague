import pygame
from pygame import Surface

from code.Background import Background
from code.Constants import WIN_WIDTH, WIN_HEIGHT


class World:
    def __init__(self, window: Surface):
        self.window = window
        self.scroll = 0
        # self.world_bg:list[Background] = []
        #
        # for i in range(0, 5):
        #     speed = 1 + (i * 2)
        #     self.world_bg.append(Background(f"World_BG_{i}", (0,0), speed))
        #     self.world_bg.append(Background(f"World_BG_{i}", (WIN_WIDTH, 0), speed))

        self.world_bg_images = []
        self.world_road_image = pygame.image.load("./assets/sprites/World/Road.png")
        self.road_y = WIN_HEIGHT - self.world_road_image.get_height()
        for i in range(0, 5):
            image = pygame.image.load(f"./assets/sprites/World/World_BG_{i}.png").convert_alpha()
            self.world_bg_images.append(image)

    def draw_bg(self):
        for i, img in enumerate(self.world_bg_images):
            speed = 1 + (i * 0.2)
            pos_x = (self.scroll * speed) % WIN_WIDTH
            self.window.blit(img, (-pos_x, 0))
            self.window.blit(img, (-pos_x + WIN_WIDTH, 0))


    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(60)
            self.draw_bg()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.scroll -= 5
            if key[pygame.K_RIGHT]:
                self.scroll += 5


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # for bg in self.world_bg:
            #     self.window.blit(bg.surf, bg.rect)
            #     #bg.move()

            pygame.display.flip()