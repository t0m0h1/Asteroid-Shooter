import pygame
import random

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

# Set the background
background = pygame.image.load("background.jpg")