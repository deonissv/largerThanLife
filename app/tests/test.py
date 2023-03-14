import pytest

from py_ltl_engine import PyBoard, PyConfig, PyNeighbourhood
from ltl.config_parser import ConfigParser


def test_neighbourhood_neumann_from_str():
    assert PyNeighbourhood.Neumann == PyNeighbourhood("NN")


def test_neighbourhood_moore_from_str():
    assert PyNeighbourhood.Moore == PyNeighbourhood("NM")


def test_neighbourhood_parse_error():
    with pytest.raises(TypeError):
        PyNeighbourhood("asd")


def test_neighbourhood_to_str():
    assert f"{PyNeighbourhood.Moore}" == "NM"
    assert f"{PyNeighbourhood.Neumann}" == "NN"


def test_config_ctor():
    config = PyConfig(1, 0, 0, (2, 3), (3, 3), PyNeighbourhood("NM"))
    board = PyBoard(3, config)
    assert board.board == [[0] * 3] * 3


def test_board_get_cell():
    config = PyConfig(1, 0, 0, (2, 3), (3, 3), PyNeighbourhood("NM"))
    board = PyBoard(3, config)
    assert board.board[0][0] == board.get_cell(0, 0)
    assert board.board[1][1] == board.get_cell(1, 1)


def test_board_set_cel():
    config = PyConfig(1, 0, 0, (2, 3), (3, 3), PyNeighbourhood("NM"))
    board = PyBoard(3, config)
    board.set_cell(1, 1, 1)
    assert board.get_cell(0, 0) == 0
    assert board.get_cell(1, 1) == 1


def test_board_update():
    config = PyConfig(1, 0, 0, (2, 3), (3, 3), PyNeighbourhood("NM"))
    board = PyBoard(3, config)
    board.cell_up(1, 0)
    board.cell_up(1, 1)
    board.cell_up(1, 2)
    board.update()
    assert board.get_cell(0, 1) == 1
    assert board.get_cell(1, 1) == 1
    assert board.get_cell(2, 1) == 1
    assert board.get_cell(1, 0) == 0
    assert board.get_cell(1, 2) == 0
