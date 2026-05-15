#!/usr/bin/env python3

import sys
# read operating system variables
import os
# manage where packages are installed
import site


# The Heart of the Script
def is_in_venv() -> bool:
    """
    Detects whether Python is running within a virtual environment

    The key: when you activate a venv, sys.prefix changes to point
    to the venv. sys.base_prefix always points to the system's original Python
    If they are different → we are inside a venv

    check VIRTUAL_ENV, which the ‘activate’ script sets
    automatically as an environment variable
    """
    prefix_changed = (sys.prefix != sys.base_prefix)
    # os.environ.get(“VIRTUAL_ENV”) returns the path to the venv
    # if it exists, or None if not. The
    # is not None = True or False
    virtual_env_set = os.environ.get("VIRTUAL_ENV") is not None
    # return true is one is true
    return prefix_changed or virtual_env_set


# What's your name?
def get_venv_name() -> str:
    """
    extract the name of the virtual environment from the VIRTUAL_ENV variable
    or from sys.prefix (both point to the venv folder)
    """
    venv_path = os.environ.get("VIRTUAL_ENV") or sys.prefix
    # /Users/neo/proyectos/matrix_env -> matrix_env
    return os.path.basename(venv_path)


# Where are you?
def get_venv_path() -> str:
    """
    returns the absolute path of the active virtual environment
    """
    # /Users/neo/proyectos/matrix_env
    return os.environ.get("VIRTUAL_ENV") or sys.prefix


# Where do you keep your tools (libraries)?
def get_site_packages_path() -> str:
    """
    Returns the path where packages are installed in the current environment

    site.getsitepackages() returns a list of paths; we take the first one
    that contains ‘site-packages’ (the one relevant for user packages)

    to demonstrate that, inside the venv, packages aren't being installed on
    the global system, but rather in a private folder within your environment
    """
    # site.getsitepackages -> returns multiple routes, not one
    paths = site.getsitepackages()
    for path in paths:
        if "site-packages" in path:
            return path
    return paths[0]


def show_outside_venv() -> None:
    """
    Output when the program runs without an active virtual environment
    warning and instructions to create one
    """
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("    python3 -m venv matrix_env")
    print("    source matrix_env/bin/activate  # On Unix")
    print(r"    matrix_env\Scripts\activate      # On Windows")
    print()
    print("Then run this program again.")


def show_inside_venv() -> None:
    """
    Output when the program runs INSIDE a virtual environment.
    Displays details about the environment
    """
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {get_venv_path()}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"    {get_site_packages_path()}")


def main() -> None:
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
