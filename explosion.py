import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size=20, color=(255, 0, 0)):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((size * 2, size * 2))
        self.rect = self.image.get_rect(center=center)
        self.color = color

    def update(self):
        pygame.draw.circle(self.image, self.color, (self.size, self.size), self.size)
        self.size += 1
        if self.size > 50:  # Adjust this to control the size of the explosion
            self.kill()
        else:
            self.image = pygame.Surface((self.size * 2, self.size * 2))
            self.rect = self.image.get_rect(center=self.rect.center)
