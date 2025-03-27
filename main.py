import pygame

pygame.init()

pygame.display.set_mode((300, 300))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
