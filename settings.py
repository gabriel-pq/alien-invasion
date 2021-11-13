class Settings:
	"""A class to store all the settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""

		# Screen settings.
		self.screen_width = 1299
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Bullet settings
		self.bullets_allowed = 70
		self.bullet_width = 30
		self.bullet_height = 60
		self.bullet_color = (60, 60, 60)

		# Alien settings
		self.fleet_drop_speed = 5

		# Ship no of respawns
		self.ship_limit = 2

		self.speedup_scale = 1.1

		# How fast the alien point values increase
		self.score_scale = 1.5
		self.initialyze_dynamic_settings()


	def initialyze_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)