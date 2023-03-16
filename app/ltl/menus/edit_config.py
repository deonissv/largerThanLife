import pygame_menu

from .base import Base
from .dynamic_menu import dynamic_menu

from ..config_parser import ConfigParser
from ..components import add_create_config, add_edit_btn, add_filename_input


@dynamic_menu()
def edit_existing_config(menu: Base, config_name: str):
    add_filename_input(menu, default=config_name)
    config = ConfigParser.parse_config(config_name)
    add_create_config(menu, config)
    add_edit_btn(menu, config_name)
    menu.add.button("Back", pygame_menu.events.BACK)
