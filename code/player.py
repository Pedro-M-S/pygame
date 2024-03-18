import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 2

    def input(self):
        keys = pygame.key.get_pressed()
        key_pressed = False

        # y direction
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not key_pressed:
            if (self.direction.x == 0 and self.direction.y == 0):
                self.direction.y = -1
                key_pressed = True
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not key_pressed:
            if (self.direction.x == 0 and self.direction.y == 0):
                self.direction.y = 1
                key_pressed = True
        else:
            self.direction.y = 0
            key_pressed = False

        # x direction
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not key_pressed:
            if (self.direction.x == 0 and self.direction.y == 0):
                self.direction.x = -1
                key_pressed = True
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not key_pressed:
            if (self.direction.x == 0 and self.direction.y == 0):
                self.direction.x = 1
                key_pressed = True
        else:
            self.direction.x = 0
            key_pressed = False

    def move(self):
        #if self.direction.magnitude() != 0:
        #    self.direction = self.direction.normalize()
        
        self.rect.center += self.direction * self.speed

    def update(self):
        self.input()
        self.move()
        