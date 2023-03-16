import pygame_menu

from .base import Base
from .dynamic_menu import dynamic_menu
from .edit_config import edit_existing_config

from ..state import state
from ..components import add_display_config
from ..handlers import handle_submit
from ..config_parser import ConfigParser


@dynamic_menu
def display_config(menu: Base):
    config_name = state.config_name
    config = ConfigParser.parse_config(config_name)

    menu.add.label(config_name)
    add_display_config(menu, config)

    menu.add.button("Edit", edit_existing_config(config_name))
    menu.add.button("Remove", pygame_menu.events.BACK).add_update_callback(
        handle_submit(lambda: ConfigParser.remove_config(config_name))
    )
    menu.add.button("Back", pygame_menu.events.BACK)
