import argparse
import os
import tomllib
from pathlib import Path


def get_version(pyproject_path: Path) -> str | None:
    try:
        with pyproject_path.open("rb", encoding="utf-8") as f:
            data = tomllib.load(f)

        # Setuptools
        if "project" in data and (version := data["project"].get("version")):
            return version

        # Poetry
        if "tool" in data and "poetry" in data["tool"] and (version := data["tool"]["poetry"].get("version")):
            return version

    except (FileNotFoundError, tomllib.TOMLDecodeError):
        pass

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pyproject", default="pyproject.toml", help="Path to pyproject.toml")
    args = parser.parse_args()

    if pyversion := get_version(Path(args.pyproject)):
        print(pyversion)
    else:
        print("No version found in pyproject.toml")
        exit(1)
