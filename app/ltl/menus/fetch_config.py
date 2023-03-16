from typing import Optional

from .base import Base

from ..py_ltl_engine import PyConfig, PyNeighbourhood


def fetch_config(menu: Base) -> Optional[PyConfig]:
    try:
        r = round(menu.get_widget("R").get_value())
        c = round(menu.get_widget("C").get_value())
        m = menu.get_widget("M").get_value()[0][1]
        s = (
            round(menu.get_widget("S_MIN").get_value()),
            round(menu.get_widget("S_MAX").get_value()),
        )
        b = (
            round(menu.get_widget("B_MIN").get_value()),
            round(menu.get_widget("B_MAX").get_value()),
        )
        n = PyNeighbourhood(menu.get_widget("N").get_value()[0][1])
        return PyConfig(r, c, m, s, b, n)
    except AttributeError:
        return None
