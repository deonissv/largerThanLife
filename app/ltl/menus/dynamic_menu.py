from typing import Callable

import pygame_menu

from .base import Base
from .apply_mouse_hover_animation import apply_mouse_hover_animation


def _get_rerender(menu: Base, fn, *args, **kwargs) -> Callable:
    def rerender(curr: pygame_menu.Menu):
        [menu.remove_widget(w) for w in curr.get_widgets()]
        fn(menu, *args, **kwargs)
        apply_mouse_hover_animation(menu)
        [m.set_onreset(lambda: rerender(curr)) for m in menu.get_submenus()]

    return rerender


def dynamic_menu(*args, **kwargs):
    if len(args) == 1 and callable(args[0]):

        def decorator(*args_, **kwargs_):
            fn = args[0]
            menu = Base()
            rerender = _get_rerender(menu, fn, *args_, **kwargs_)
            menu.set_onbeforeopen(
                lambda _, curr: rerender(curr),
            )
            return menu

        return decorator

    def decorator(fn: Callable):
        def inner(*args_, **kwargs_):
            menu = Base(*args, **kwargs)
            rerender = _get_rerender(menu, fn, *args_, **kwargs_)
            menu.set_onbeforeopen(
                lambda _, curr: rerender(curr, *args),
            )
            return menu

        return inner

    return decorator
