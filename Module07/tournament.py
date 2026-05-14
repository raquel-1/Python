#!/usr/bin/env python3

from typing import List, Tuple
from ex0.factory import FlameFactory, AquaFactory, CreatureFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # double loop so everyone can compete against each other
    # select firt opponent
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            # unpack the tuple
            fact1, strat1 = opponents[i]
            fact2, strat2 = opponents[j]

            # FlameFactory ....
            name1_clss = fact1.__class__.__name__
            name2_clss = fact2.__class__.__name__

            # dictionary to obtain the name of the pokemon
            mapping = {
                "FlameFactory": "Flameling",
                "AquaFactory": "Aquabub",
                "HealingCreatureFactory": "Sproutling",
                "TransformCreatureFactory": "Shiftling"
            }
            # c1_name = Flameling
            pokemon1_name = mapping.get(name1_clss, "Creature1")
            pokemon2_name = mapping.get(name2_clss, "Creature2")

            # create objects using a factory
            pokemon1 = fact1.create_base(pokemon1_name)
            pokemon2 = fact2.create_base(pokemon2_name)

            print(pokemon1.describe())
            print(" vs.")
            print(pokemon2.describe())
            print(" now fight!")

            try:
                # implement the strategies
                strat1.act(pokemon1)
                strat2.act(pokemon2)
            except ValueError as e:
                # canceling the tournament if there is a strategic error
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    # Factory
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    trans_fact = TransformCreatureFactory()

    # Strategy
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("\nTournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_fact, normal), (heal_fact, defensive)])

    print("\n\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_fact, aggressive), (heal_fact, defensive)])

    print("\n\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_fact, normal),
        (heal_fact, defensive),
        (trans_fact, aggressive),
    ])
