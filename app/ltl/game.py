import pygame
import pygame_menu

from .assets import icon

from .menus import main_menu

BACKGROUND_COLOR = (200, 200, 250)
BOARD_LENGTH = 70

FPS = 60


class Game:
    _window_width: int
    _window_height: int
    _screen: pygame.surface
    _menu: pygame_menu.Menu

    def __init__(self, window_width: int, window_height: int):
        pygame.init()
        pygame.display.set_caption("Larger than Life")
        pygame.display.set_icon(icon)

        self._window_width = window_width
        self._window_height = window_height
        self._screen = pygame.display.set_mode(
            [self._window_width, self._window_height]
        )
        self._menu = main_menu()

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            self._menu.update(events)
            self._menu.draw(self._screen)
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
