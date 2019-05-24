class Settings():
    """ a class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (153, 204, 255)

        # Ship settings
        self.ship_speed_factor = 1.5