#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("\nTesting Creature with healing capability")
    print(" base:")
    base = factory.create_base("Sproutling")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evol = factory.create_evolved("Bloomelle")
    print(evol.describe())
    print(evol.attack())
    print(evol.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("\n\nTesting Creature with transform capability")
    print(" base:")
    base = factory.create_base("Shiftling")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evol = factory.create_evolved("Morphagon")
    print(evol.describe())
    print(evol.attack())
    print(evol.transform())
    print(evol.attack())
    print(evol.revert())


if __name__ == "__main__":
    test1 = HealingCreatureFactory()
    test2 = TransformCreatureFactory()
    test_healing(test1)
    test_transform(test2)
