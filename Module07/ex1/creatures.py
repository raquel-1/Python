#!/usr/bin/env python3

from typing import Optional
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")
        self._power = "Vine Whip"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"

    def heal(self, target: Optional[str] = None) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")
        self._power = "Petal Dance"

    def attack(self) -> str:
        return self._name + " uses " + self._power + "!"

    def heal(self, target: Optional[str] = None) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal")
        # Without this, _transformed does not exist
        TransformCapability.__init__(self)

    def attack(self) -> str:
        # transform = True
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        # normal = False
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal/Dragon")
        # Without this, _transformed does not exist
        TransformCapability.__init__(self)

    def attack(self) -> str:
        # transform = True
        if self._transformed:
            return "Morphagon performs a boosted strike!"
        # normal = False
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."
