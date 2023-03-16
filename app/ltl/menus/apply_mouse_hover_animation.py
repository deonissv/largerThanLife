import pygame_menu


def apply_mouse_hover_animation(menu: pygame_menu.Menu) -> None:
    for widget in menu.get_widgets():
        widget.set_onmouseover(lambda w, _: w.select(True, True))
        widget.set_onmouseleave(lambda w, _: w.select(False, False))
