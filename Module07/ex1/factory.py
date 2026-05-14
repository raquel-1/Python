#!/usr/bin/env python3

from ex0.factory import CreatureFactory
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> Sproutling:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Bloomelle:
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> Shiftling:
        return Shiftling(name)

    def create_evolved(self, name: str) -> Morphagon:
        return Morphagon(name)
