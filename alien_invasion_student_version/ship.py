import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.transform.scale(pygame.image.load('images/ship1.bmp'), (49,72))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """ Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Update the ship's center value, not the rect
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


        if self.moving_up and self.rect.top < self.rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        #Update rect object from self.center.
        self.rect.centerx = self.center



    def blitme(self):
        """ Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


