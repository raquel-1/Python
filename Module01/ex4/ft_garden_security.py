#!/usr/bin/env python3

class Plant:
    """Represents a plant with a name, starting height and  starting age."""

    def __init__(self, name: str, height: float, my_age: int) -> None:
        self._name: str = name
        self.height = 0.0
        self.my_age = 0
        self.set_height(height, init=True)
        self.set_age(my_age, init=True)

    def set_height(self, height: float, init: bool = False) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            self._height = 0.0
        else:
            self._height = height
            if not init:
                print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int, init: bool = False) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            self._my_age = 0
        else:
            self._my_age = age
            if not init:
                print(f"Age updated: {self._my_age} days")

    def get_age(self) -> int:
        return self._my_age

    def show(self) -> None:
        """Displays the plant information in a formatted way."""
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._my_age} days old"
        )

    def custom_show(self, word: str) -> None:
        """Same as show def but with Current:"""
        print(f"{word}: ", end="")
        self.show()

    def grow(self) -> None:
        if self._name.capitalize() == "Rose":
            self._height += 0.8
        elif self._name.capitalize() == "Sunflower":
            self._height += 0.9
        elif self._name.capitalize() == "Cactus":
            self._height += 0.2
        else:
            self._height += 0.5

    def age(self) -> None:
        self._my_age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    flower1 = Plant("Rose", 15, 10)
    flower1.custom_show("Plant created")
    print("")
    flower1.set_height(25)
    flower1.set_age(30)
    print("")
    flower1.set_height(-25)
    flower1.set_age(-30)
    print("")
    flower1.custom_show("Current state")
