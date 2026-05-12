#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (
            self._name + " is a " + self._creature_type + " type Creature"
        )


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")
        self._power = "Ember"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")
        self._power = "Flamethrower"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"


class Aquabub(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")
        self._power = "Water Gun"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"


class Torragon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")
        self._power = "Hydro Pump"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"
