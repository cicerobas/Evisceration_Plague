import pygame
from pygame import Surface

from code.Constants import PLAYER_ANIMATIONS, ZOMBIE_ANIMATIONS


def split_sprites(sprite_sheet: Surface, frame_data: tuple) -> list[Surface]:
    frames: list[Surface] = []
    for i in range(frame_data[2]):
        frame = sprite_sheet.subsurface((i * frame_data[0], 0, frame_data[0], frame_data[1]))
        frames.append(frame)

    return frames

class Animations:
    def __init__(self, entity_name: str):
        self.entity_name = entity_name
        self.animations: dict[str, tuple] = PLAYER_ANIMATIONS if self.entity_name == "Player" else ZOMBIE_ANIMATIONS
        self.animation_frames: dict[str, list[Surface]] = {}
        self.load_animations()

    def load_animations(self):
        for animation in self.animations:
            sprite_sheet = pygame.image.load(f"./assets/sprites/{self.entity_name}/{animation}.png").convert_alpha()
            split_frames = split_sprites(sprite_sheet, self.animations[animation])
            self.animation_frames.update({animation: split_frames})

    def get(self, name: str) -> list[Surface]:
        return self.animation_frames.get(name, None)
