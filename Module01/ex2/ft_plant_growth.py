#!/usr/bin/env python3

class Plant:
    """Represents a plant with a name, height and age."""

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        """Displays the plant information in a formatted way."""
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        if self.name.capitalize() == "Rose":
            self.height += 0.8
        elif self.name.capitalize() == "Sunflower":
            self.height += 0.9
        else:
            self.height += 0.5

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    flower1 = Plant("Rose", 25, 30)
    start_h = flower1.height
    print("=== Garden Plant Growth ===")
    for n in range(1, 8):
        print(f"=== Day {n} ===")
        flower1.show()
        flower1.grow()
        flower1.age()
    print(f"Growth this week: {round(flower1.height - start_h, 1)}cm")
