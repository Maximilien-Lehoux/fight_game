import pygame
from pygame.locals import *

from background_color import *
from background_picture import *
from fight_game_constant import *
from generate_display import *

pygame.init()

# Create main window
window = pygame.display.set_mode(window_size)

# Create background sky blue
background_sky = BackgroundColor(color_sky, color_sky_location, window)
window.blit(background_sky.background_colorful, background_sky.location_background_colorful)

# Create clouds
background_cloud = BackgroundPicture(background_cloud, location_background_cloud, SPRITE_SIZE*2)
window.blit(background_cloud.background_picture, background_cloud.location_background_picture)

level = Level("level_structure")
level_structure = level.generate()
level.display_decor(window, background_cloud, "c")

finish = False

while not finish:
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True

    pygame.display.flip()

pygame.display.flip()
pygame.display.quit()