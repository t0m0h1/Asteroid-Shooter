import pygame
import random
from player import Player
from laser import Laser

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

# Set the background
background = pygame.image.load("images/background.jpg")

clock = pygame.time.Clock()


# sprite group for the player's lasers
all_sprites = pygame.sprite.Group()
player_lasers = pygame.sprite.Group()



# Instantiate the player
player = Player()





while True:
    # Set the background color
    screen.fill((0, 0, 0))
    # Set the background image
    screen.blit(background, (0, 0))

    # Set the player
    player.draw(screen) #start position

    # move the player
    player.update()

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                laser = Laser(player.rect.centerx, player.rect.top)
                    all_sprites.add(laser)
                    lasers.add(laser)
            # Handle other key events if needed
