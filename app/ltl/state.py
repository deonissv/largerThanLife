from typing import Dict, Optional

import pygame
import random

from collections import defaultdict

from py_ltl_engine import PyBoard, PyConfig

BOARD_LENGTH = 70
FPS = 60


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class State(metaclass=Singleton):
    _config: Optional[PyConfig]
    _config_name: str
    _colors: Dict[int, pygame.Color]
    _board: PyBoard
    _valid_board: bool
    _board_running: bool
    _fps: int
    _counter: int

    def __init__(self):
        self._colors = defaultdict(
            lambda: pygame.Color(random.sample(range(0, 255), 3))
        )
        self._valid_board = False
        self._board_running = False
        self._config = None
        self._counter = 0
        self._fps = 15

    @property
    def config(self) -> Optional[PyConfig]:
        return self._config

    @config.setter
    def config(self, value: PyConfig) -> None:
        self._valid_board = False
        self._config = value

    def set_config(self, value: PyConfig) -> None:
        self.config = value

    def randomize_config(self) -> None:
        """
        Set the config to a random config
        """
        self.config = PyConfig.randomize()

    @property
    def config_name(self) -> str:
        return self._config_name

    @config_name.setter
    def config_name(self, value: str) -> None:
        self._config_name = value

    def set_config_name(self, value: str) -> None:
        self.config_name = value

    @property
    def fps(self) -> int:
        return self._fps

    @fps.setter
    def fps(self, value: int) -> None:
        self._fps = value

    def set_fps(self, value) -> None:
        self.fps = value

    @property
    def board(self) -> PyBoard:
        if not self._valid_board:
            self._board = PyBoard(BOARD_LENGTH, self.config)
            self._valid_board = True
        return self._board

    @property
    def is_board_running(self) -> bool:
        return self._board_running

    def start_board(self) -> None:
        self._board_running = True

    def stop_board(self) -> None:
        self._board_running = False

    def toggle_board(self) -> None:
        self._board_running = not self.is_board_running

    def update_board(self) -> bool:
        if self.is_board_running:
            self._counter += 1
            if self._counter % round(FPS / self._fps) == 0:
                self.board.update()
                return True
        return False

    def color(self, cell_state: int) -> pygame.Color:
        return self._colors[cell_state]


state = State()
