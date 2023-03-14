import pygame_menu


def add_filename_input(menu: pygame_menu.Menu, name: str = "Name: ", default=""):
    menu.add.text_input(name, default=default, maxchar=12, textinput_id="NAME")
