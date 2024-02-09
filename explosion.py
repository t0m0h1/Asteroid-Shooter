import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size=20, color=(255, 255, 0)):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=center)
        self.color = color

    def update(self):
        pygame.draw.circle(self.image, self.color, (self.size, self.size), self.size)
        self.size += 1 # grow the explosion
        if self.size > 30:  # exoplosion size limit
            self.kill()
