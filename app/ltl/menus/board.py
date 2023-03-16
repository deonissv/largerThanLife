import pygame_menu

from .base import Base
from .dynamic_menu import dynamic_menu
from .save_manual_config import save_manual_config

from ..components import add_grid
from ..handlers import handle_submit, handle_scroll
from ..state import state

MAX_FPS = 60
MIN_FPS = 1
DISPLAY_CONFIG_ID = "DISPLAY_CONFIG"


@dynamic_menu
def board(menu: Base, savable: bool = False):
    add_grid(menu)
    wrapper = menu.add.frame_v(324, 699, margin=0, padding=0).translate(350, 0)
    wrapper._pack_margin_warning = False
    start_btn = menu.add.button("Start", lambda: state.toggle_board())
    start_btn.get_decorator().add_callable(
        lambda _, w: w.set_title("Stop")
        if state.is_board_running
        else w.set_title("Start"),
    )
    random_btn = menu.add.button("Random", lambda: state.board.randomize())
    reset_btn = menu.add.button("Reset Grid", lambda: state.board.reset())
    fps_slider = menu.add.range_slider(
        "FPS",
        state.fps,
        (MIN_FPS, MAX_FPS),
        1,
        value_format=lambda x: str(round(x)),
        onchange=lambda value: state.set_fps(value),
    )
    save_btn = menu.add.button("Save", save_manual_config()) if savable else None

    fps_slider.add_update_callback(handle_scroll(MIN_FPS, MAX_FPS))
    back_btn = menu.add.button("Back", pygame_menu.events.BACK)
    back_btn.add_update_callback(handle_submit(lambda: state.stop_board()))
    wrapper.pack(
        [
            w
            for w in [start_btn, random_btn, reset_btn, fps_slider, save_btn, back_btn]
            if w is not None
        ],
        align=pygame_menu.locals.ALIGN_CENTER,
        vertical_position=pygame_menu.locals.POSITION_CENTER,
    )
