import pygame
from pygame.locals import *

from fight_game_constant import *

background_cloud = "pictures/nuage.png"
location_background_cloud = [SPRITE_SIZE*3, SPRITE_SIZE]


class BackgroundPicture:
    """create background from saved image"""
    def __init__(self, file_background, location_background_picture, size):
        self.background_picture = pygame.image.load(file_background).convert_alpha()
        self.background_picture = pygame.transform.scale(self.background_picture, (size, size))
        self.location_background_picture = location_background_picture