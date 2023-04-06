import sys
import pygame

class MyGame:
    """class for game attirbutes"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200 , 500))
        self.bg_color = (133, 204, 216)
        pygame.display.set_caption("my game")
        self.ball = Ball(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ball.bltime()
            pygame.display.flip()

class Ball:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initiliaze the ship and set satrating position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship and its rect.
        self.image = pygame.image.load('image/football.bmp')
        self.rect = self.image.get_rect()

        #start each ne ship at the bottom corer of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def bltime(self):
        """"draw ship in its current location."""
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    ai = MyGame()
    ai.run_game()