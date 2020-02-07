import pygame
from pygame.locals import *

color_sky = "#9ce4ff"
color_sky_location = [0, 0]


class BackgroundColor:
    """create background colorful"""
    def __init__(self, background_color, location_background_colorful, window):
        self.background_colorful = pygame.Surface(window.get_size())
        self.background_colorful = self.background_colorful.convert()
        self.background_colorful.fill(pygame.Color(background_color))
        self.location_background_colorful = location_background_colorful