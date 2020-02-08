import pygame
from pygame.locals import *

from fight_game_constant import *

file_character1 = "pictures/rectangle_bleu.jpg"
file_character2 = "pictures/rectangle_vert.png"

location_character1 = [SPRITE_SIZE*4, SPRITE_SIZE*12]
location_character2 = [SPRITE_SIZE*20, SPRITE_SIZE*12]

class Characters:
    """Create main character"""
    def __init__(self, picture, item_location, width, height):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (width, height))
        self.rectangle = self.picture.get_rect()
        self.rectangle.topleft = item_location
        window.blit(self.picture, self.rectangle)