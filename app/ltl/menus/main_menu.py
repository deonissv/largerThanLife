import pygame_menu

from .static_menu import static_menu
from .choose_configuration import choose_configuration
from .existing_configurations import existing_configurations


@static_menu()
def main_menu(self):
    self.add.button("Play", choose_configuration())
    self.add.button("Existing configurations", existing_configurations())
    self.add.button("Quit", pygame_menu.events.EXIT)
