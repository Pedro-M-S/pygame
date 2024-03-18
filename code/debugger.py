import pygame
pygame.init()
font = pygame.font.Font(None, 12)

def debug(info, surface, x = 10, y = 10):
    display_surface = surface
    debugger_surface = font.render(str(info), False, (255, 255, 255))
    debugger_rect = debugger_surface.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surface, (0, 0, 0), debugger_rect)
    display_surface.blit(debugger_surface, debugger_rect)