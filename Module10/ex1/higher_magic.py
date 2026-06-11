#!/usr/bin/env python3
from collections.abc import Callable


# def spell(target: str, power: int) -> str
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """
    Receives two spells and returns a new function
    """
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        combi1 = spell1(target, power)
        combi2 = spell2(target, power)
        return (combi1, combi2)
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    """
    Receive a spell and a multiplier.
    Return a new spell that multiplies the original power
    """
    def amplified_power(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return amplified_power


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """
    Cast a spell conditionally
    """
    def caster(target: str, power: int) -> str:
        """
        returns the result of the spell
        """
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """
    Create a spell sequence
    """
    def list_sequence(target: str, power: int) -> list[str]:
        """
        Returns a list containing the results of all spells
        """
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return list_sequence


if __name__ == "__main__":
    # basic spell
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    # test condition
    def is_powerful_enough(target: str, power: int) -> bool:
        return power >= 50

    print("Testing spell combiner...")
    # mix fireball and heal
    combined = spell_combiner(fireball, heal)
    result_mix = combined("Dragon", 20)
    print(f"Combined spell result: {result_mix[0]}, {result_mix[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10 -> {fireball('Orc', 10)}")
    print(f"Amplified: {10 * 3} -> {mega_fireball('Orc', 10)}")

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(is_powerful_enough, fireball)
    print(f"Casting with power 20: {conditional_spell('Reptilian', 20)}")
    print(f"Casting with power 60: {conditional_spell('Reptilian', 60)}")

    print("\nTesting spell sequence...")
    spell_list: list[Callable[[str, int], str]] = [fireball, heal, fireball]
    sequence = spell_sequence(spell_list)
    print(f"Sequence results: {sequence('Dinosaur', 15)}")
