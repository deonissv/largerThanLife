import pygame_menu

from .base import Base
from .static_menu import static_menu

from ..components import add_create_config, add_save_btn, add_filename_input


@static_menu
def create_config(menu: Base):
    add_filename_input(menu)
    add_create_config(menu)
    add_save_btn(menu)
    menu.add.button("Back", pygame_menu.events.BACK)
