import pygame_menu

from .base import Base
from .dynamic_menu import dynamic_menu
from .create_config import create_config
from .display_config import display_config

from ..state import state
from ..handlers import handle_submit
from ..config_parser import ConfigParser


@dynamic_menu()
def existing_configurations(menu: Base) -> None:
    for config_name in ConfigParser.parse_config_names():
        display_config_menu = display_config()
        menu.add.button(config_name, display_config_menu).add_update_callback(
            handle_submit(lambda w: state.set_config_name(w.get_title()))
        )

    menu.add.button("New", create_config())
    menu.add.button("Back", pygame_menu.events.BACK)
