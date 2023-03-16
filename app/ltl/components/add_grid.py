from typing import Tuple, Optional

import pygame
import pygame_menu

from ..menus import Base

from ..state import state

BOARD_LENGTH = 70
GRID_CELL_WIDTH = 10


def add_grid(menu: Base):
    sc = pygame.Surface(
        (BOARD_LENGTH * GRID_CELL_WIDTH, BOARD_LENGTH * GRID_CELL_WIDTH)
    )

    grid = menu.add.surface(
        sc, selectable=True, float=True, float_origin_position=True, margin=0, padding=0
    )
    grid.add_draw_callback(_draw_callback)
    grid.add_update_callback(_update_callback)


def _draw_callback(widget: pygame_menu.widgets.Widget, _menu: pygame_menu.Menu) -> None:
    for x in range(0, BOARD_LENGTH):
        for y in range(0, BOARD_LENGTH):
            cell_state = state.board.get_cell(x, y)
            cell_color = (
                pygame.Color("white") if cell_state == 0 else state.color(cell_state)
            )
            _draw_cell(widget.get_surface(), x, y, cell_color)
    state.update_board()


def _draw_cell(
    sc: pygame.Surface, x: int, y: int, bg_colog: pygame.Color = pygame.Color("white")
):
    rect = pygame.Rect(
        x * GRID_CELL_WIDTH, y * GRID_CELL_WIDTH, GRID_CELL_WIDTH, GRID_CELL_WIDTH
    )
    pygame.draw.rect(sc, bg_colog, rect)
    pygame.draw.rect(sc, pygame.Color("black"), rect, 1)


def _update_callback(
    events: [pygame.event], widget: pygame_menu.widgets.Widget, menu: pygame_menu.Menu
) -> None:
    if _is_mouse_over(widget):
        cell_coord = _get_cell_coord(widget)
        if cell_coord is not None:
            _markup_active_cell(widget.get_surface(), *cell_coord)
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                cell_coord = _get_cell_coord(widget)
                if cell_coord is not None:
                    state.board.cell_up(*cell_coord)
            if event.button == pygame.BUTTON_RIGHT:
                cell_coord = _get_cell_coord(widget)
                if cell_coord is not None:
                    state.board.cell_down(*cell_coord)
    menu.force_surface_update()


def _get_cell_coord(widget: pygame_menu.widgets.Widget) -> Optional[Tuple[int, int]]:
    rel_mouse_pos_x = pygame.mouse.get_pos()[0] - widget.get_position()[0]
    rel_mouse_pos_y = pygame.mouse.get_pos()[1] - widget.get_position()[1]

    coord_x = rel_mouse_pos_x // GRID_CELL_WIDTH
    coord_y = rel_mouse_pos_y // GRID_CELL_WIDTH

    if coord_x < BOARD_LENGTH and coord_y < BOARD_LENGTH:
        return coord_x, coord_y
    return None


def _markup_active_cell(sc: pygame.Surface, x, y):
    rect = pygame.Rect(
        x * GRID_CELL_WIDTH,
        y * GRID_CELL_WIDTH,
        GRID_CELL_WIDTH,
        GRID_CELL_WIDTH,
    )
    pygame.draw.rect(sc, pygame.Color("white"), rect, 1)


def _is_mouse_over(widget: pygame_menu.widgets.Widget) -> bool:
    mouse_pos = pygame.mouse.get_pos()
    rect = widget.get_rect()
    return (
        rect.x < mouse_pos[0] < rect.x + rect.w
        and rect.y < mouse_pos[1] < rect.y + rect.h
    )
