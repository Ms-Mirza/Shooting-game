import pygame as p
from pygame.sprite import Sprite

import sys
import os

# Add this function at the top of ship.py 
def resource_path(relative_path):
    """Get absolute path — works for both dev and PyInstaller .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get its rect
        self.image = p.image.load(resource_path('image/ship.bmp'))
        
        # resize imapge
        self.image = p.transform.scale(self.image,(65,75))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """"center the ship on the screen"""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's center value, not rect
        # restrict the ship to go out of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)