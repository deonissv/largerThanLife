import json
import os
from json import JSONDecodeError

from pathlib import Path
from typing import Optional

from py_ltl_engine import PyConfig, PyNeighbourhood

RR_MAX = 10
CC_MAX = 25
MAX = 65535


class ConfigParser:
    _configs_folder = Path(__file__).parent.parent.parent / "configs"

    @classmethod
    def config_file(cls, filename: str) -> str:
        return f"{cls._configs_folder / filename}.json"

    @classmethod
    def parse_config(cls, config_name: str) -> Optional[PyConfig]:
        with open(cls.config_file(config_name), "r") as f:
            try:
                config_data = json.load(f)
            except JSONDecodeError:
                return None
        try:
            rr = config_data["rr"]
            cc = config_data["cc"]
            mm = config_data["mm"]
            ss_min = config_data["ss"][0]
            ss_max = config_data["ss"][1]
            bb_min = config_data["bb"][0]
            bb_max = config_data["bb"][1]
            nn = PyNeighbourhood(config_data["nn"])

            if not (
                (0 <= rr <= RR_MAX)
                and (0 <= cc <= CC_MAX)
                and (mm == 0 or mm == 1)
                and (0 <= ss_min <= MAX)
                and (0 <= ss_max <= MAX)
                and (0 <= bb_min <= MAX)
                and (0 <= bb_max <= MAX)
                and (ss_min <= ss_max)
                and (bb_min <= bb_max)
            ):
                return None

            return PyConfig(rr, cc, mm, (ss_min, ss_max), (bb_min, bb_max), nn)

        except (AttributeError, KeyError, ValueError):
            return None

    @classmethod
    def parse_config_names(cls) -> list[str]:
        all_configs_path = f"{cls._configs_folder}"
        configs = []
        for config_filename in os.listdir(all_configs_path):
            if os.path.isfile(cls._configs_folder / config_filename):
                config_name = config_filename.removesuffix(".json")
                if cls.parse_config(config_name) is not None:
                    configs.append(config_name)
        return configs

    @classmethod
    def save_config(cls, config_name: str, config: PyConfig) -> None:
        with open(f"{cls._configs_folder / config_name}.json", "w") as f:
            json.dump(config.__dict__, f, indent=2)

    @classmethod
    def remove_config(cls, config_name: str) -> None:
        os.remove(f"{cls._configs_folder / config_name}.json")
