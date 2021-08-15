import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # Resize the ship image.
        self.image = pygame.transform.scale(self.image, (53, 72))
        self.rect = self.image.get_rect()
        # Start each new ship the the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Braw the ship at its current location."""
        self.screen.blit(self.image, self.rect)