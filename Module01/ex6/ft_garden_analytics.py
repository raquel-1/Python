#!/usr/bin/env python3

class Plant:
    # Nested Class Stats
    class Stats:
        def __init__(self) -> None:
            self._count_grow: int = 0
            self._count_age: int = 0
            self._count_show: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self._count_grow} grow, "
                f"{self._count_age} age, {self._count_show} show"
            )

    def __init__(self, name: str, height: float, my_age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._my_age: int = 0
        self.set_height(height, init=True)
        self.set_age(my_age, init=True)
        # We use Any so that Mypy will allow the switch to TreeStats later
        self._stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_year(days: int) -> bool:
        if days >= 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    # setters
    def set_height(self, height: float, init: bool = False) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            if not init:
                print(f"Height updated: {self._height}cm")

    def set_age(self, age: int, init: bool = False) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._my_age = age
            if not init:
                print(f"Age updated: {self._my_age} days")

    # getters
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._my_age

    # methods
    def grow(self) -> None:
        self._stats._count_grow += 1
        if self._name.capitalize() == "Rose":
            self._height += 8
        elif self._name.capitalize() == "Sunflower":
            self._height += 30
        else:
            self._height += 0.9

    def age(self) -> None:
        self._stats._count_age += 1
        self._my_age += 20

    def show(self) -> None:
        self._stats._count_show += 1
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._my_age} days old"
        )


class Tree(Plant):
    # define specific  Stats for Tree
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._count_shade: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._count_shade} shade")

        def increment_shade(self) -> None:
            self._count_shade += 1

    def __init__(
        self, name: str, height: float, my_age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, my_age)
        self._trunk_diameter: float = float(trunk_diameter)
        # override the stats object with the Tree-specific one
        self._stats: Tree.TreeStats = self.TreeStats()

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm"
            f" long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


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
        super().show()
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        my_age: int,
        color: str,
        count_seeds: int
    ) -> None:
        super().__init__(name, height, my_age, color)
        self._count_seeds: int = count_seeds

    def bloom(self) -> None:
        super().bloom()
        self._count_seeds += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._count_seeds}")


def display_stats(plant: Plant) -> None:
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year(400)}")
    print("")
    print("=== Flower")
    flower1 = Flower("Rose", 15, 10, "red")
    flower1.show()
    print("[statistics for Rose]")
    display_stats(flower1)
    print("[asking the rose to grow and bloom]")
    flower1.bloom()
    flower1.grow()
    flower1.show()
    print("[statistics for Rose]")
    display_stats(flower1)
    print("")
    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    print("[statistics for Oak]")
    display_stats(tree1)
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    display_stats(tree1)
    print("")
    print("=== Seed")
    seed1 = Seed("Sunflower", 80, 45, "yellow", 0)
    seed1.show()
    print("[make sunflower grow, age and bloom]")
    seed1.grow()
    seed1.age()
    seed1.bloom()
    seed1.show()
    print("[statistics for Sunflower]")
    display_stats(seed1)
    print("")
    print("=== Anonymous")
    dontknow = Plant.create_anonymous()
    dontknow.show()
    print("[statistics for Unknown plant]")
    display_stats(dontknow)
