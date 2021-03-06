import pygame
from pygame import sprite
import json

class Object(sprite.Sprite):
    def __init__(self, entity, fps, speed, display, pos):
        super().__init__()

        # Basic information about an object
        self.name = entity
        self.filepath = f"assets/images/{entity}.png"
        self.sprite_sheet = pygame.image.load(self.filepath).convert()
        self.meta_data = self.filepath.replace('png', 'json')
        self.display = display
        self.pos = pos

        with open(self.meta_data) as f: 
            self.data = json.load(f)
        f.close()

        # This list holds all the sprites gathered from the spritesheet
        self.sprites = []
        self.sprite_index = 0

        # This speed controls when to switch from sprite animation to the
        #   next animation in the spritesheet
        self.animate_speed = fps * speed
        self.animation_tick = 0

        # Parsing all the sprites contained in the spritesheet
        for index in range(len(self.data['frames'])):
            self.sprites.append(self.fetch_sprite(f'{self.name}{index}.png'))


    def __len__(self):
        return len(self.sprites)


    def fetch_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, width, height = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = pygame.Surface((width, height))
        image.set_colorkey((0,0,0))
        image.blit(self.sprite_sheet,(0, 0),(x, y, width, height))
        return image


    def update(self):
        self.animation_tick += 1
        if self.animation_tick >= self.animate_speed:
            self.animation_tick = 0
            self.sprite_index = (self.sprite_index + 1) % len(self.sprites)
        self.display.blit(self.sprites[self.sprite_index], self.pos)
