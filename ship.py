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

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Ship speed
        self.ship_speed = 1.5
        # Adjust 'x' rect variable because it supports only integers
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updating the ship's position based on the movement flag"""
        # Update the 'x' value of the ship
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        # Update the 'x' rect value
        self.rect.x = self.x
