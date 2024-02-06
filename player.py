import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Set the image size to 50x50
        self.rect = self.image.get_rect()
        self.speed = 5
        

    def draw(self, screen, position):
        screen.blit(self.image, self.rect)
        self.rect.x = position[0]
        self.rect.y = position[1]
