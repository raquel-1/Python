#!/usr/bin/env python3

import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
# ok
print(f"Testing create_air: {alchemy.create_air()}")
# error not in __init__ from alchemy
print("Now show that not all functions can be reached")
print("This will raise an exception!")
# Mypy ignore error
earth = alchemy.create_earth()  # type: ignore[attr-defined]
print(f"Testing the hidden create_earth: {earth}")
