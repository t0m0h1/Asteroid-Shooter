import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) # Set the size of the player
        self.rect = self.image.get_rect() # Get the rectangle of the player to be used for positioning
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left < 0:
                self.rect.left = 0  # Limit movement to the left edge
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.right > 800:
                self.rect.right = 800  # Limit movement to the right edge


    def draw(self, screen):
        screen.blit(self.image, self.rect) # Draw the player on the screen
