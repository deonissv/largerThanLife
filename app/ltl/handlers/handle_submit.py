from inspect import signature
from typing import Callable, Any

import pygame
import pygame_menu


def handle_submit(
    fn: Callable, *fn_args
) -> Callable[
    [[pygame.event.Event], pygame_menu.widgets.Widget, pygame_menu.Menu], Any
]:
    def _handle_submit(
        events: list[pygame.event.Event],
        widget: pygame_menu.widgets.Widget,
        menu: pygame_menu.Menu,
    ):
        for event in events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == pygame.BUTTON_LEFT
            ) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                params = signature(fn).parameters
                match len(params) - len(fn_args):
                    case 0:
                        fn(*fn_args)
                    case 1:
                        fn(widget, *fn_args)
                    case 2:
                        fn(widget, menu, *fn_args)
                    case _:
                        raise Exception("incorrect number of arguments")
                break
            # if (
            #     event.type == pygame.MOUSEBUTTONDOWN
            #     and event.button == pygame.BUTTON_LEFT
            # ):
            #     fn(*fn_args)
            #     break
            #
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #     fn(*fn_args)
            #     break

    return _handle_submit
