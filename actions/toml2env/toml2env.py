#!/usr/bin/env python
import os
import sys
import tomllib
from typing import Union


def dict_to_env_vars(d: dict[str, Union[str, dict[str, any]]], prefix: str = '') -> dict[str, str]:
    env_vars = {}
    for key, value in d.items():
        if isinstance(value, dict):
            env_vars.update(dict_to_env_vars(value, prefix + key.upper() + '_'))
        else:
            env_vars[prefix + key.upper()] = value
    return env_vars


def main():
    toml_file = sys.argv[1]
    print(toml_file)
    with open(toml_file, 'rb') as f:
        content = tomllib.load(f)
    print(content)
    env_vars = dict_to_env_vars(content)
    print(env_vars)
    print(os.environ)
    print(os.environ['GITHUB_ENV'])
    with open(os.environ['GITHUB_ENV'], 'a') as f:
        for key, value in env_vars.items():
            f.write(f'{key}={value}\n')


if __name__ == "__main__":
    main()
