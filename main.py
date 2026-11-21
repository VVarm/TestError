"""Deliberately broken example for practicing code review."""

from config_loader import load_config
from calculator import calculate


def main():
    config = load_config()
    print(calculate(config["expression"]))


if __name__ == "__main__":
    main()
