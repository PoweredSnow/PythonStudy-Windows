import pygame
import sys


class KeystrokeTest:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("键盘输入测试")

    def run(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if 0 <= event.key <= 0x10ffff:
            print(chr(event.key))
        else:
            print(event.key)

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        pygame.display.flip()


if __name__ == '__main__':
    test = KeystrokeTest()
    test.run()
