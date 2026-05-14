#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            trans = cast(TransformCapability, creature)
            print(trans.transform())
            print(creature.attack())
            print(trans.revert())
        else:
            raise ValueError(
                f"Invalid Creature '{creature._name}' "
                "for this aggressive strategy"
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            heal = cast(HealCapability, creature)
            print(creature.attack())
            print(heal.heal())
        else:
            raise ValueError(
                f"Invalid Creature '{creature._name}' "
                "for this defensive strategy"
                )
