import pygame
from pygame.locals import *

from fight_game_constant import *

file_character1 = "pictures/rectangle_bleu.jpg"
file_character2 = "pictures/rectangle_vert.png"

character_location_wall = [0, 0]
# location_character1 = [SPRITE_SIZE*4, SPRITE_SIZE*12]
# location_character2 = [SPRITE_SIZE*20, SPRITE_SIZE*12]


class Player(pygame.sprite.Sprite):
    """Create character"""
    def __init__(self, file_character, width_size, height_size, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.picture = pygame.image.load(file_character).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (width_size, height_size))
        self.rectangle = self.picture.get_rect()
        self.rectangle.x = x
        self.rectangle.y = y

    def move_right(self):
        self.rectangle.x += self.velocity

    def move_left(self):
        self.rectangle.x -= self.velocity

    def jump(self):
        height_jump = 0
        while height_jump != 25:
            self.rectangle.y -= 3
            height_jump += 1

