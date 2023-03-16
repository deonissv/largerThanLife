import pygame_menu

from py_ltl_engine import PyConfig


def add_display_config(menu: pygame_menu.Menu, config: PyConfig):
    m = "Enabled" if config.mm else "Disabled"
    menu.add.label(f"r: {config.rr}")
    menu.add.label(f"c: {config.cc}")
    menu.add.label(f"m: {m}")
    menu.add.label(f"s: {config.ss}")
    menu.add.label(f"b: {config.bb}")
    menu.add.label(f"n: {config.nn}")
