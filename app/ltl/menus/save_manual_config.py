import pygame_menu.events

from . import Base
from .dynamic_menu import dynamic_menu

from ..state import state
from ..components import add_filename_input, add_display_config, add_save_btn


@dynamic_menu
def save_manual_config(menu: Base):
    add_filename_input(menu)
    add_display_config(menu, state.config)
    add_save_btn(menu)
    menu.add.button("Back", pygame_menu.events.BACK)
