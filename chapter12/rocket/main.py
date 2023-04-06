import sys
import pygame

from rocket import Rocket

class Game():
    """general class for the game"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 620))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("rocket game")
        self.rocket = Rocket(self)
    def run_game(self):
        """game main loop"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        """key presses"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

    def _check_keyup(self, event):
        """for key release"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.bltime()
        pygame.display.flip()

if __name__ == "__main__":
    my_game = Game()
    my_game.run_game()