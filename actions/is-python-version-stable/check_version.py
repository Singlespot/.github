import argparse
import os

from packaging.version import parse, InvalidVersion

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
            gh.write(f"stable={is_stable}\n")
            gh.write(f"dev={version.is_devrelease}\n")
            gh.write(f"post={version.is_postrelease}\n")
            gh.write(f"pre={version.is_prerelease}\n")
