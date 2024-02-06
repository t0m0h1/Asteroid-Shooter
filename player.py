import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Set the image size to 50x50
        self.rect = self.image.get_rect()
        self.speed = 5
        

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self, screen, position):
        screen.blit(self.image, self.rect)
        self.rect.x = position[0]
        self.rect.y = position[1]
