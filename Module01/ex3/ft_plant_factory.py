#!/usr/bin/env python3

class Plant:
    """Represents a plant with a name, starting height and  starting age."""

    def __init__(self, name: str, s_height: float, s_age: int) -> None:
        self.name: str = name
        self.s_height: float = s_height
        self.s_age: int = s_age

    def show(self) -> None:
        """Displays the plant information in a formatted way."""
        print(
            f"{self.name}: {round(self.s_height, 1)}cm, {self.s_age} days old"
            )

    def create_show(self) -> None:
        """Same as show def but with Created:"""
        print("Created: ", end="")
        self.show()

    def grow(self) -> None:
        if self.name.capitalize() == "Rose":
            self.s_height += 0.8
        elif self.name.capitalize() == "Sunflower":
            self.s_height += 0.9
        elif self.name.capitalize() == "Cactus":
            self.s_height += 0.2
        else:
            self.s_height += 0.5

    def age(self) -> None:
        self.s_age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    flower1 = Plant("Rose", 25.0, 30)
    flower1.create_show()
    flower2 = Plant("Oak", 200.0, 365)
    flower2.create_show()
    flower3 = Plant("Cactus", 5.0, 90)
    flower3.create_show()
    flower4 = Plant("Sunflower", 80.0, 45)
    flower4.create_show()
    flower5 = Plant("Fern", 15.0, 120)
    flower5.create_show()
