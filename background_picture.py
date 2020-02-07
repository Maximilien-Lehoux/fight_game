import pygame
from pygame.locals import *

from fight_game_constant import *


class BackgroundPicture:
    """create background from saved image"""
    def __init__(self, background):
        self.background_picture = pygame.image.load(background).convert_alpha()
        self.background_picture = pygame.transform.scale(self.background_picture, (SPRITE_SIZE, SPRITE_SIZE))