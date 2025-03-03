import argparse
import os

from packaging.version import parse, InvalidVersion


def to_bool_str(value: bool) -> str:
    return "true" if value else "false"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()

    try:
        version = parse(args.version)
    except InvalidVersion:
        print("Invalid version")
        exit(1)
    else:
        is_stable = not (version.is_devrelease or version.is_postrelease or version.is_prerelease)
        with open(os.environ["GITHUB_OUTPUT"], "a") as gh:
            gh.write(f"stable={to_bool_str(is_stable)}\n")
            gh.write(f"dev={to_bool_str(version.is_devrelease)}\n")
            gh.write(f"post={to_bool_str(version.is_postrelease)}\n")
            gh.write(f"pre={to_bool_str(version.is_prerelease)}\n")
