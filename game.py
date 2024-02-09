import pygame
import random
from player import Player
from laser import Laser
from asteroid import Asteroid

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

score = 0
score_font = pygame.font.Font(None, 36)

# Set the background
background = pygame.image.load("images/background.jpg")

clock = pygame.time.Clock()


# sprite groups for all sprites, lasers, and asteroids
all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()



for i in range(8):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)


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


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        laser = Laser(player.rect.centerx, player.rect.top)
        all_sprites.add(laser)
        lasers.add(laser)

    # Update the lasers and draw them
    all_sprites.update()
    all_sprites.draw(screen)
    
    for laser in lasers:
        laser.update()
        if laser.rect.bottom < 0:
            laser.kill()


    # Check for collisions between asteroids and lasers
    collisions = pygame.sprite.groupcollide(asteroids, lasers, True, True)

    # If there is a collision, add a new asteroid and update the score
    for collision in collisions:
        score += 1
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    # Draw the score
    score_text = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10)) # this will blit the score on the screen

                
    # update the remaining asteroids
    asteroids.update()


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
