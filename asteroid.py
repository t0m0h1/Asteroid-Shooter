import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroid.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.x = random.randint(0, 800)
            self.rect.y = random.randint(-100, -40)