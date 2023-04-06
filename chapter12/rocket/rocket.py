import pygame

class Rocket:
    def __init__(self, my_game):
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()
        #load image of rocket
        self.image = pygame.image.load('image/rocket.bmp')
        self.image = pygame.transform.scale(self.image,(29,55))
        self.rect = self.image.get_rect()
        #put ship in center of screen
        self.rect.center = self.screen_rect.center
        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def bltime(self):
        """draw ship in current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -=1