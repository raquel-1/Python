#!/usr/bin/env python3
"""
Exercise 0: Entering the Matrix - Construct.
"""

import os
import site
import sys


def is_in_venv() -> bool:
    """Detects whether Python is running within a virtual environment."""
    prefix_changed: bool = (sys.prefix != sys.base_prefix)
    virtual_env_set: bool = os.environ.get("VIRTUAL_ENV") is not None
    return prefix_changed or virtual_env_set


def get_venv_name() -> str:
    """Extracts the name of the virtual environment folder."""
    venv_path: str = os.environ.get("VIRTUAL_ENV") or sys.prefix
    return os.path.basename(venv_path)


def get_venv_path() -> str:
    """Returns the absolute path of the active virtual environment."""
    return os.environ.get("VIRTUAL_ENV") or sys.prefix


def get_site_packages_path() -> str:
    """Returns the path where packages are installed in the current env."""
    paths: list[str] = site.getsitepackages()
    for path in paths:
        if "site-packages" in path:
            return path
    return paths[0] if paths else ""


def show_outside_venv() -> None:
    """Output when the program runs without an active virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("    python -m venv matrix_env")
    print("    source matrix_env/bin/activate # On Unix")
    print(r"    matrix_env\Scripts\activate      # On Windows")
    print("\nThen run this program again.")


def show_inside_venv() -> None:
    """Output when the program runs INSIDE a virtual environment."""
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {get_venv_path()}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    print(f"    {get_site_packages_path()}")


def main() -> None:
    """Main execution control."""
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
