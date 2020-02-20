import pygame
from pygame.locals import *

from fight_game_constant import *
from characters import *


# Create class to represent game
class Game:
    def __init__(self):
        self.player1 = Player(file_character1, int(SPRITE_SIZE / 1.8), int(SPRITE_SIZE * 1.4), SPRITE_SIZE * 4,
                              SPRITE_SIZE * 12)
        self.player2 = Player(file_character2, int(SPRITE_SIZE / 1.8), int(SPRITE_SIZE * 1.4), SPRITE_SIZE * 20,
                              SPRITE_SIZE * 12)
        self.pressed = {}
