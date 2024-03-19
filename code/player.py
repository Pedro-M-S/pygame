import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacles_group):
        super().__init__(group)
        self.image = pygame.image.load('../graphics/player/walk_down_idle/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.obstacles_group = obstacles_group

        self.import_player_assets()

        self.status = 'start_sleep'

        self.frame_index = 0
        self.animation_speed = 0.1

    
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'sleep' in self.status:
                self.status = self.status + '_idle'
        """
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')
        """
    

    def import_player_assets(self):
        player_path = '../graphics/player/'
        self.animations = {'walk_up': [], 'walk_down': [], 'walk_left': [], 'walk_right': [],
                           'start_sleep': [], 'take_damage': [],
                           'walk_up_idle': [], 'walk_down_idle': [], 'walk_left_idle': [], 'walk_right_idle': []}
        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)
        
    def input(self):
        keys = pygame.key.get_pressed()
        key_pressed = self.direction.x != 0 and self.direction.y != 0

        # y direction
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not key_pressed:
            self.direction.y = -1
            self.status = 'walk_up'
            key_pressed = True
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not key_pressed:
            self.direction.y = 1
            self.status = 'walk_down'
            key_pressed = True
        else:
            self.direction.y = 0
            key_pressed = False

        # x direction
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not key_pressed:
            self.direction.x = -1
            self.status = 'walk_left'
            key_pressed = True
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not key_pressed:
            self.direction.x = 1
            self.status = 'walk_right'
            key_pressed = True
        else:
            self.direction.x = 0
            key_pressed = False

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for obstacle in self.obstacles_group:
                if obstacle.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = obstacle.rect.left
                    if self.direction.x < 0:
                        self.rect.left = obstacle.rect.right
                    
        if direction == 'vertical':
            for obstacle in self.obstacles_group:
                if obstacle.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = obstacle.rect.top
                    if self.direction.y < 0:
                        self.rect.top = obstacle.rect.bottom

    def animation(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.input()
        self.get_status()
        self.animation()
        self.move()
        
        