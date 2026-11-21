"""Load settings from the JSON file next to this module."""

import json
from pathlib import Path


def load_config():
    config_path = Path(__file__).with_name("config.json")
    with config_path.open(encoding="utf-8") as file:
        return json.load(file)
