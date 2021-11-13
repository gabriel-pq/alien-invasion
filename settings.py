class Settings:
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""

		# Screen settings.
		self.screen_width = 1299
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Bullet settings
		self.bullet_speed = 1.5
		self.bullets_allowed = 70
		self.bullet_width = 30
		self.bullet_height = 60
		self.bullet_color = (60, 60, 60)

		# Alien settings
		self.alien_speed = 1
		self.fleet_drop_speed = 5

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		# Ship settings
		self.ship_speed = 3
		self.ship_limit = 2
