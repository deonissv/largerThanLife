from enum import Enum

class PyNeighbourhood(Enum):
    def __init__(self, neighbourhood: str) -> PyNeighbourhood: ...
    def __str__(self) -> str: ...

class PyConfig(object):
    def __init__(
        self,
        rr: int,
        cc: int,
        mm: int,
        ss: tuple[int, int],
        bb: tuple[int, int],
        nn: PyNeighbourhood,
    ) -> None: ...
    def randomize(self, seed: int = ...) -> PyConfig: ...
    @property
    def rr(self) -> int: ...
    @property
    def cc(self) -> int: ...
    @property
    def mm(self) -> int: ...
    @property
    def ss(self) -> tuple[int, int]: ...
    @property
    def bb(self) -> tuple[int, int]: ...
    @property
    def nn(self) -> PyNeighbourhood: ...

class PyBoard(object):
    def __init__(self, size: int, config: PyConfig): ...
    @property
    def board(self) -> list[list[int]]: ...
    def reset(self): ...
    def get_cell(self, x: int, y: int) -> int: ...
    def set_cell(self, x: int, y: int, value: int) -> None: ...
    def randomize(self, seed: int = ...): ...
    def cell_up(self, x: int, y: int) -> None: ...
    def cell_down(self, x: int, y: int) -> None: ...
    def update(self) -> None: ...
