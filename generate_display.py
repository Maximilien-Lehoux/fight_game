import pygame
from pygame.locals import *

from fight_game_constant import *


class Level:
    """Class to create a level"""
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """Method to generate the level according to the file.
        We create a general list, containing a list per line to display"""
        # Open the file
        with open(self.file, "r") as file:
            level_structure = []
            # We browse the lines of the file
            for line in file:
                level_line = []
                # We browse the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the "\ n" at the end of the line
                    if sprite != '\n':
                        # We add the sprite to the line list
                        level_line.append(sprite)
                # We add the line to the level list
                level_structure.append(level_line)
            # We save this structure
            self.structure = level_structure
            return level_structure

    def display_decor(self, window, item_structure, letter):
        """Method for displaying the level in function
        of the structure list returned by generate()"""
        # We browse the level list
        line_number = 0
        for line in self.structure:
            # we browse the line lists
            case_number = 0
            for sprite in line:
                # We calculate the actual position in pixels
                x = case_number * SPRITE_SIZE
                y = line_number * SPRITE_SIZE
                if sprite == letter:
                    window.blit(item_structure.background_picture, (x, y))
                # elif sprite == 'g':  # g = guardian
                    # window.blit(item_arrive.picture, (x, y))
                case_number += 1
            line_number += 1

    def display_character(self, window, item_structure, letter):
        """Method for displaying the level in function
        of the structure list returned by generate()"""
        # We browse the level list
        line_number = 0
        for line in self.structure:
            # we browse the line lists
            case_number = 0
            for sprite in line:
                # We calculate the actual position in pixels
                x = case_number * SPRITE_SIZE
                y = line_number * SPRITE_SIZE
                if sprite == letter:
                    window.blit(item_structure.picture, (x, y))
                # elif sprite == 'g':  # g = guardian
                    # window.blit(item_arrive.picture, (x, y))
                case_number += 1
            line_number += 1