import pygame

from ..state import state
from ..handlers import handle_submit
from ..menus import fetch_config, Base
from ..py_ltl_engine import PyConfig
from ..config_parser import ConfigParser


def add_edit_btn(menu: Base, config_name: str, config: PyConfig = None, title="Save"):
    menu.add.button(title, None).add_update_callback(
        handle_submit(_submit, menu, config_name)
    )


def _submit(menu: Base, config_name: str):
    new_config_name = menu.get_widget("NAME").get_value()
    if new_config_name != "":
        # @TODO
        config = fetch_config(menu)
        if config_name != new_config_name:
            ConfigParser.remove_config(config_name)
            state.set_config_name(new_config_name)
        ConfigParser.save_config(config_name, config)
        menu.reset(1)
    else:
        menu.get_widget("NAME").set_border(
            3, pygame.color.Color(255, 0, 0), position="position-south"
        )
