import pygame_menu

from .base import Base
from .board import board
from .dynamic_menu import dynamic_menu

from ..state import state
from ..handlers import handle_submit
from ..config_parser import ConfigParser


@dynamic_menu()
def choose_existing_configurations(menu: Base):
    for config_name in ConfigParser.parse_config_names():
        menu.add.button(config_name, board()).add_update_callback(
            handle_submit(
                lambda w: state.set_config(ConfigParser.parse_config(w.get_title()))
            )
        )
    menu.add.button("Back", pygame_menu.events.BACK)
