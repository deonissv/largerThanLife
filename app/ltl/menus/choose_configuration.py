import pygame_menu

from .base import Base
from .board import board
from .static_menu import static_menu
from .create_manual_config import create_manual_config
from .choose_existing_configurations import choose_existing_configurations

from ..state import state
from ..handlers import handle_submit


@static_menu()
def choose_configuration(menu: Base):
    menu.add.button("Create random", board(True)).add_update_callback(
        handle_submit(lambda: state.randomize_config())
    )
    menu.add.button("Create manual", create_manual_config())
    menu.add.button("Choose existing", choose_existing_configurations())
    menu.add.button("Back", pygame_menu.events.BACK)
