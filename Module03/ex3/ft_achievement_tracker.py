#!/usr/bin/env python3

import random


ACHIEVEMENTS_LIST = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Alchemist',
    'Hidden Path Finder', 'Legendary Hero', 'Merchant King', 'Monster Tamer',
    'Fast Learner'
]


def gen_player_achievements() -> set[str]:
    n_ach = random.randint(1, len(ACHIEVEMENTS_LIST))
    selec_ach = random.sample(ACHIEVEMENTS_LIST, n_ach)
    return set(selec_ach)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("")
    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("")
    # We combine the sets of the 4 players
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print("")
    # Common of the 4 players
    common_ach = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_ach}")
    print("")
    # For each player, spot the achievements no one else has
    print("Only Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(alice, charlie, dylan))
    print("Only Charlie has:", charlie.difference(bob, alice, dylan))
    print("Only Dylan has:", dylan.difference(bob, charlie, alice))
    print("")
    # For each player, list the missing achievements to have them all
    print("Alice  is missing:", set(ACHIEVEMENTS_LIST).difference(alice))
    print("Bob  is missing:", set(ACHIEVEMENTS_LIST).difference(bob))
    print("Charlie  is missing:", set(ACHIEVEMENTS_LIST).difference(charlie))
    print("Dylan  is missing:", set(ACHIEVEMENTS_LIST).difference(dylan))
