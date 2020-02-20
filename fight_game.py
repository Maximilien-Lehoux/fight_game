import pygame
from pygame.locals import *

from background_color import *
from background_picture import *
from fight_game_constant import *
from generate_display import *
from characters import *
from game import *

pygame.init()

# Create main window
window = pygame.display.set_mode(window_size)

# Generate level
level = Level("level_structure")
level_structure = level.generate()

# Create background sky blue
background_sky = BackgroundColor(color_sky, color_sky_location, window)
window.blit(background_sky.background_colorful, background_sky.location_background_colorful)

# Create clouds
background_cloud = BackgroundPicture(file_background_cloud, location_background_cloud, SPRITE_SIZE*2, SPRITE_SIZE*2)
level.display_decor(window, background_cloud, "c")

# Create background ground
background_ground = BackgroundPicture(file_background_ground, location_background_ground, window_width + SPRITE_SIZE,
                                      window_height)
window.blit(background_ground.background_picture, background_ground.location_background_picture)

# Create platform
platform_wood = BackgroundPicture(file_background_ground, location_platform_wood, SPRITE_SIZE+1, int(SPRITE_SIZE/1.5))
level.display_decor(window, platform_wood, "w")

# to charge game
game = Game()

finish = False

while not finish:

    window.blit(background_sky.background_colorful, background_sky.location_background_colorful)
    window.blit(background_ground.background_picture, background_ground.location_background_picture)
    level.display_decor(window, background_cloud, "c")
    level.display_decor(window, platform_wood, "w")
    window.blit(game.player1.picture, game.player1.rectangle)
    window.blit(game.player2.picture, game.player2.rectangle)

    # to check move left or right
    if game.pressed.get(pygame.K_RIGHT):
        game.player2.move_right()
        if game.pressed.get(pygame.K_d):
            game.player1.move_right()
        if game.pressed.get(pygame.K_a):
            game.player1.move_left()

    if game.pressed.get(pygame.K_LEFT):
        game.player2.move_left()
        if game.pressed.get(pygame.K_a):
            game.player1.move_left()
        if game.pressed.get(pygame.K_d):
            game.player1.move_right()

    if game.pressed.get(pygame.K_d) and not (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_LEFT)):
        game.player1.move_right()
    if game.pressed.get(pygame.K_a) and not (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_LEFT)):
        game.player1.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            finish = True

        # if player touch keyboard
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # touch jump detection
            if event.key == pygame.K_UP:
                game.player2.jump()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


pygame.display.flip()
pygame.display.quit()