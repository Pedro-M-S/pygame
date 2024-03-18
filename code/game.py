import pygame, sys
from settings import *

from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH * 3, HEIGHT * 3))
        pygame.display.set_caption('pygame_lolo')
        self.clock = pygame.time.Clock()

        self.level = Level()

        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            
            self.level.run()
            self.screen.blit(pygame.transform.scale(self.level.display_surface,(WIDTH * 3, HEIGHT * 3)), (0, 0))
            
            pygame.display.update()
            self.clock.tick(FPS)
        