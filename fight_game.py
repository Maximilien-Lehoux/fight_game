import pygame
from pygame.locals import *

from background_color import *
from background_picture import *
from fight_game_constant import *
from generate_display import *

pygame.init()

# Create main window
window = pygame.display.set_mode(window_size)

# Generate level
level = Level("level_structure")
level_structure = level.generate()

# Create background sky blue
background_sky = BackgroundColor(color_sky, color_sky_location, window)
window.blit(background_sky.background_colorful, background_sky.location_background_colorful)

# Create background ground
background_ground = BackgroundPicture(file_background_ground, location_background_ground, window_width + SPRITE_SIZE,
                                      window_height)
window.blit(background_ground.background_picture, background_ground.location_background_picture)

# Create platform
platform_wood = BackgroundPicture(file_background_ground, location_platform_wood, SPRITE_SIZE+1, int(SPRITE_SIZE/1.5))
level.display_decor(window, platform_wood, "w")

# Create clouds
background_cloud = BackgroundPicture(file_background_cloud, location_background_cloud, SPRITE_SIZE*2, SPRITE_SIZE*2)
level.display_decor(window, background_cloud, "c")


finish = False

while not finish:
    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True

    window.blit(background_sky.background_colorful, background_sky.location_background_colorful)
    window.blit(background_ground.background_picture, background_ground.location_background_picture)
    level.display_decor(window, background_cloud, "c")
    level.display_decor(window, platform_wood, "w")
    pygame.display.flip()

pygame.display.flip()
pygame.display.quit()