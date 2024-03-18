import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        #self.display_surface = pygame.display.set_mode((WIDTH * 3, HEIGHT * 3))
        self.display_surface = pygame.Surface((WIDTH, HEIGHT))
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()

        self.background = pygame.image.load('../graphics/background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.background_rect = self.background.get_rect()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # []
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x, y), self.visible_sprites)
                    


    def run(self):
        self.display_surface.blit(self.background, self.background_rect)
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()