import pygame
from pygame.locals import *

from fight_game_constant import *

file_background_cloud = "pictures/nuage.png"
location_background_cloud = [0, 0]

file_background_ground = "pictures/sol_terre.png"
location_background_ground = [-10, window_height-(SPRITE_SIZE*2)]

file_platform_wood = "pictures/texture_bois.jpg"
location_platform_wood = [0, 0]


class BackgroundPicture:
    """create background from saved image"""
    def __init__(self, file_background, location_background_picture, width, height):
        self.background_picture = pygame.image.load(file_background).convert_alpha()
        self.background_picture = pygame.transform.scale(self.background_picture, (width, height))
        self.location_background_picture = location_background_picture

# je t'aime mon doudou d'amour, travail bien ton jeux est deja super :D #