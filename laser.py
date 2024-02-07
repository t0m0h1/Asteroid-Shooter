import pygame 

# pygame surface to create the laser


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 5))  # Adjust the size of the laser
        self.image.fill((0, 0, 255))  # Fill the laser surface with a red color
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = 4

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the laser when it goes off-screen
