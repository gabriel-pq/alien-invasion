import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        ###################################
        # USED FOR MANUAL-DRAW OF THE BULLET
        # self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        ###################################

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/bullet.png')
        # Resize the ship image.
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect.top = ai_game.ship.rect.top - self.settings.bullet_height + 15

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up to the screen."""

        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed

        # Update the rect position
        self.rect.y = self.y

    # USED FOR MANUAL-DRAW OF THE BULLET
    # def draw_bullet(self):
    #     """Draw the bullet to the screen."""
    #     pygame.draw.rect(self.screen, self.color, self.rect)

    def blitme(self):
        """Draw the bullet at its current location."""

        self.screen.blit(self.image, self.rect)
