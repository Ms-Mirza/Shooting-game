import sys
import pygame as p
from pygame.sprite import Sprite
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #  Initialize pygame settings and screen object.
    p.init()
    ai_settings = Settings()
    screen = p.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    p.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    # Sstart the main loop for the game
    alien = Alien(ai_settings, screen)

    # create the fleet of alien
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # start the main loop for the game.
    while True:
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)
        
run_game()







