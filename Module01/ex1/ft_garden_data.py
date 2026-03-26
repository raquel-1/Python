#!/usr/bin/env python3

"""
Garden Data Organizer - manages and displays information about plants.
"""


class Plant:
    """Represents a plant with a name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        """Displays the plant information in a formatted way."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    flower1 = Plant("Rose", 25, 30)
    flower2 = Plant("Sunflower", 80, 45)
    flower3 = Plant("Cactus", 15, 120)
    flower1.show()
    flower2.show()
    flower3.show()
