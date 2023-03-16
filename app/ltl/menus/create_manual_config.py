import pygame_menu

from .base import Base
from .board import board
from .dynamic_menu import dynamic_menu
from .fetch_config import fetch_config

from ..state import state
from ..handlers import handle_submit
from ..components import add_create_config


@dynamic_menu
def create_manual_config(menu: Base) -> None:
    add_create_config(menu, state.config)

    menu.add.button("Proceed", board(True)).add_update_callback(
        handle_submit(lambda: state.set_config(fetch_config(menu)))
    )
    menu.add.button("Back", pygame_menu.events.BACK)
