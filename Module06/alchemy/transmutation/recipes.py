#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# relative
from ..elements import create_air  # noqa: E402
# absolute
from alchemy.potions import strength_potion  # noqa: E402
# fire in root
from elements import create_fire  # noqa: E402


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew '"
        + create_air() + "' and '" + strength_potion()
        + "' mixed with '" + create_fire() + "'"
    )
