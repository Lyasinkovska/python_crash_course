import sys
import pygame
from bullet import Bullet
from settings import Settings


def check_keydown_events(event, ai_settins, screen, ship, bullets):
    """Respond to keydown events."""
    if event.key == pygame.K_UP:
        # Move ship to the right
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move ship to the left
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settins, screen, ship, bullets)



def check_keyup_events(event, ship):
    """ Respond to key releases."""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """ Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """ Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through a loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Redraw all the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets, ai_settings):
    """ Update position of bullets and get rid of old bullets"""
    # Update bullet positions.
    bullets.update()
    ai_settings = Settings()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.left > ai_settings.screen_width:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship , bullets):
    """Fire a bullet if limit not reached yet. """
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

