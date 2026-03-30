#!/usr/bin/env python3

class Plant:
    """Represents a plant with a name, starting height and  starting age."""

    def __init__(self, name: str, height: float, my_age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._my_age: int = 0
        self.set_height(height, init=True)
        self.set_age(my_age, init=True)

    def set_height(self, height: float, init: bool = False) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            if not init:
                print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int, init: bool = False) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
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
        elif self._name.capitalize() == "Tomato":
            self._height += 2.1
        else:
            self._height += 0.9

    def age(self) -> None:
        self._my_age += 1


class Flower(Plant):
    def __init__(
        self, name: str, height: float, my_age: int, color: str
    ) -> None:
        super().__init__(name, height, my_age)
        self._color: str = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        """Displays the flower information in a formatted way."""
        super().show()
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, my_age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, my_age)
        self._trunk_diameter: float = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm"
            f" long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        """Displays the Tree information in a formatted way."""
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        my_age: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, my_age)
        self._harvest_season: str = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        """Displays the Vegetable information in a formatted way."""
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1 = Flower("Rose", 15, 10, "red")
    flower1.show()
    print("[asking the rose to bloom]")
    flower1.bloom()
    flower1.show()
    print("")
    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("")
    print("=== Vegetable")
    tomato1 = Vegetable("Tomato", 5, 10, "April", 0)
    tomato1.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21):
        tomato1.grow()
        tomato1.age()
    tomato1.show()
