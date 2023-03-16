from typing import Callable, Any

import pygame
import pygame_menu

from ..utils import clip


def handle_scroll(
    min_val: int, max_val: int
) -> Callable[
    [[pygame.event.Event], pygame_menu.widgets.Widget, pygame_menu.Menu], Any
]:
    def handle_scroll_(
        events: list[pygame.event.Event],
        widget: pygame_menu.widgets.Widget,
        _menu: pygame_menu.Menu,
    ):
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                delta = event.y
                new_value = clip(min_val, widget.get_value() + delta, max_val)
                widget.set_value(new_value)
                widget.change()

    return handle_scroll_
