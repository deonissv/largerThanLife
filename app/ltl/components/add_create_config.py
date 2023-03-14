import pygame_menu

from ..py_ltl_engine import PyConfig
from ..handlers import handle_scroll, handle_double_slider_change


def add_create_config(menu: pygame_menu.Menu, config: PyConfig = None):
    menu.add.range_slider(
        "R",
        10 if config is None else config.rr,
        (1, 10),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="R",
    ).add_update_callback(handle_scroll(1, 10))

    menu.add.range_slider(
        "C",
        0 if config is None else config.cc,
        (0, 25),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="C",
    ).add_update_callback(handle_scroll(0, 25))

    menu.add.selector(
        "M ", [("Enabled", 1), ("Disabled", 0)], selector_id="M"
    ).set_value(1 if config is not None and config.mm == 0 else 0)

    s_min_slider = menu.add.range_slider(
        "",
        123 if config is None else config.ss[0],
        (1, 255),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="S_MIN",
    ).translate(-120, 0)
    s_min_slider.add_update_callback(handle_scroll(1, 255))

    s_max_slider = menu.add.range_slider(
        "S",
        212 if config is None else config.ss[1],
        (1, 255),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="S_MAX",
        range_margin=(50, 0),
        float=True,
    ).translate(120, 0)
    s_max_slider.add_update_callback(handle_scroll(1, 255))

    handle_double_slider_change(menu, s_min_slider, s_max_slider, 1, 255)

    b_min_slider = menu.add.range_slider(
        "",
        123 if config is None else config.bb[0],
        (1, 255),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="B_MIN",
    ).translate(-120, 0)
    b_min_slider.add_update_callback(handle_scroll(1, 255))

    b_max_slider = menu.add.range_slider(
        "B",
        170 if config is None else config.bb[1],
        (1, 255),
        1,
        value_format=lambda x: str(round(x)),
        rangeslider_id="B_MAX",
        range_margin=(50, 0),
        float=True,
    ).translate(120, 0)
    b_max_slider.add_update_callback(handle_scroll(1, 255))

    handle_double_slider_change(menu, b_min_slider, b_max_slider, 1, 255)

    menu.add.selector(
        "N ", [("Moore", "NM"), ("Neumann", "NN")], selector_id="N"
    ).set_value(1 if config is not None and f"{config.nn}" == "NN" else 0)
