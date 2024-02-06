import pygame

class player:
    def __init__(self):
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.y_change = 0
        self.playerImg = pygame.image.load("player.png")