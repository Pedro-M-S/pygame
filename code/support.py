import pygame
from os import walk


def import_folder(path):
    img_surfaces = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            img_surfaces.append(image_surface)
    return img_surfaces
        
 