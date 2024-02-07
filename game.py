import pygame
import random
from player import Player

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

# Set the background
background = pygame.image.load("images/background.jpg")

clock = pygame.time.Clock()

# Set the player
player = Player()


while True:
    # Set the background color
    screen.fill((0, 0, 0))
    # Set the background image
    screen.blit(background, (0, 0))

    # Set the player
    middle = [375, 500]
    player.draw(screen, middle) #start position

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
            # Handle other key events if needed
