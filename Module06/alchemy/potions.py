#!/usr/bin/env python3
import sys
from pathlib import Path

# from within the package (relative import)
from .elements import create_earth, create_air
# root project elements.py
from elements import create_fire, create_water

sys.path.insert(0, str(Path(__file__).parent.parent))


# easy import of create_earth and create_air
def healing_potion() -> str:
    return (
        "Healing potion brewed with '" + create_earth()
        + "' and '" + create_air() + "'"
    )


# from root elements.py
def strength_potion() -> str:
    return (
        "Strength potion brewed with '" + create_fire()
        + "' and '" + create_water() + "'"
    )
