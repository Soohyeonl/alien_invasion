import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, 'Play')

    status = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, status)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, status, sb, play_button, ship, aliens, bullets)

        if status.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, status, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, status, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, status, sb, ship, aliens, bullets, play_button)


run_game()
