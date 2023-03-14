import pygame_menu

from ..utils import clip


def handle_double_slider_change(
    menu,
    min_slider: pygame_menu.widgets.RangeSlider,
    max_slider: pygame_menu.widgets.RangeSlider,
    min_value: int,
    max_value: int,
):
    def handle_double_slider_change_min(val) -> None:
        new_value = clip(min_value, max(val, max_slider.get_value()), max_value)
        max_slider.set_value(new_value),
        max_slider.draw(menu.surface)

    def handle_double_slider_change_max(val) -> None:
        new_value = clip(min_value, min(val, min_slider.get_value()), max_value)
        min_slider.set_value(new_value),
        min_slider.draw(menu.surface)

    min_slider.set_onchange(handle_double_slider_change_min)
    max_slider.set_onchange(handle_double_slider_change_max)
