import pygame
from pygame import sprite
import json

class Object(sprite.Sprite):
    def __init__(self, entity):
        self.name = entity
        self.filepath = f"assets/images/{entity}.png"
        self.sprite_sheet = pygame.image.load(self.filepath).convert()
        self.meta_data = self.filepath.replace('png', 'json')

        with open(self.meta_data) as f: 
            self.data = json.load(f)
        f.close()

        self.sprites = []
        self.index = 0

        # Parsing all the sprites contained in the spritesheet
        for index in range(len(self.data['frames'])):
            self.sprites.append(self.fetch_sprite(f'{self.name}{index}.png'))


    def __len__(self):
        return len(self.sprites)


    def fetch_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = pygame.Surface((w, h))
        image.set_colorkey((0,0,0))
        image.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return image


    def get_sprite(self, index): 
        return self.sprites[index]
