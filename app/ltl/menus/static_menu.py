from typing import Callable

from .base import Base
from .apply_mouse_hover_animation import apply_mouse_hover_animation


def static_menu(*args, **kwargs):
    if len(args) == 1 and callable(args[0]):

        def decorator(*args_, **kwargs_):
            fn = args[0]
            menu = Base()
            fn(menu, *args_, **kwargs_)
            apply_mouse_hover_animation(menu)
            return menu

        return decorator

    def decorator(fn: Callable):
        def inner(*args_, **kwargs_):
            menu = Base(*args, **kwargs)
            fn(menu, *args_, **kwargs_)
            apply_mouse_hover_animation(menu)
            return menu

        return inner

    return decorator
