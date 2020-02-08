import pygame
from pygame.locals import *

SPRITE_SIZE = 60
FPS = 30

window_height = 15 * SPRITE_SIZE
window_width = 25 * SPRITE_SIZE
window_size = (window_width, window_height)

# Create main window
window = pygame.display.set_mode(window_size)