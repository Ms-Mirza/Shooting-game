class Settings():
    '''A class to store all settings for alien invasion'''
    def __init__(self):
        '''Initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230,230,220)

        # Ship settings
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 10
        

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 255,0,0
        self.bullets_allowed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 0.4 
        self.bullet_speed_factor = 2

        # Scoring
        self.alien_points = 5

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        '''Increasing speed settings'''
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
       

"""Solve the error for highscore."""

    