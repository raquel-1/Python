#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory

def test_factory(factory: CreatureFactory, name1: str, name2: str) -> str:
    print("\nTesting factory")
    base = factory.create_base(name1)
    print(base.describe())
    print(base.attack())
    evol = factory.create_evolved(name2)
    print(evol.describe())
    print(evol.attack())

def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> str:
    print("\nTesting battle")
    base1 = factory1.create_base("Flameling")
    print(base1.describe())
    print(" vs.")
    base2 = factory2.create_base("Aquabub")
    print(base2.describe())
    print(" fight")
    print(base1.attack())
    print(base2.attack())

if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame, "Flameling", "Pyrodon")
    test_factory(aqua, "Aquabub", "Torragon")
    battle(flame, aqua)
