import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        image = pygame.transform.scale(pygame.image.load('images/ship.bmp'), (49,72))
        self.image = pygame.transform.rotate(image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center.

        self.midleft = float(self.rect.left)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            # Updatethe ship's center value, not the rect
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor

        #Update rect object from self.center.
        self.rect.left = self.midleft

    def blitme(self):
        """ Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


