import pygame
import pygame_menu

from ..menus import fetch_config
from ..handlers import handle_submit
from ..config_parser import ConfigParser


def add_save_btn(menu: pygame_menu.Menu, title="Save"):
    menu.add.button(title, None).add_update_callback(handle_submit(_submit, menu))


def _submit(menu):
    config_name = menu.get_widget("NAME").get_value()
    if config_name != "":
        config = fetch_config(menu)
        ConfigParser.save_config(config_name, config)
        menu.reset(1)
    else:
        menu.get_widget("NAME").set_border(
            3, pygame.color.Color(255, 0, 0), position="position-south"
        )
