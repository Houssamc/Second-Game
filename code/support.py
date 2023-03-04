from os import walk
import pygame


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = (pygame.transform.scale(pygame.image.load(full_path), (500, 350))).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def enemy_import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = (pygame.transform.scale(pygame.image.load(full_path), (250, 300))).convert_alpha()
            flipped_surf = pygame.transform.flip(image_surf, True, False)
            surface_list.append(flipped_surf)

    return surface_list
