import pygame
import pygame_menu

BOARD_ID = "BOARD"

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 700

BACKGROUND_COLOR = (200, 200, 250)


class Base(pygame_menu.Menu):
    def __init__(
        self,
        *args,
        title="",
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        theme=None,
        **kwargs,
    ):
        self._theme = (
            theme
            if theme is not None
            else pygame_menu.Theme(
                background_color=BACKGROUND_COLOR,
                title=False,
                widget_font=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                widget_font_color=(0, 0, 0),
                widget_margin=(0, 15),
                widget_selection_effect=pygame_menu.widgets.SimpleSelection(),
            )
        )

        super().__init__(title, width, height, theme=self._theme, *args, **kwargs)

    @property
    def surface(self) -> pygame.Surface:
        return self._widgets_surface
