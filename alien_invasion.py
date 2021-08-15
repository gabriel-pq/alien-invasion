import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Create a display window and set the dimension of the window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Set the 'title' of the window.
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    @staticmethod
    def _check_events():
        # Respond to keypress and mouse events.
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Render the ship on the background.
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Redraw everything on the screen during each pass through the loop.
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
