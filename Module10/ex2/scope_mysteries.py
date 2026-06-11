#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    """
    Returns a function that counts how many times it has been called
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Returns a function that accumulates power over time
    """
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


def enchantment_factory(
        enchantment_type: str
) -> Callable[[str], str]:
    """
    Returns a function that takes the name of an object as an argument
    and returns the text
    """

    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
    Create a memory management system with private storage.
    """

    memory_private_dict: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory_private_dict[key] = value

    def recall(key: str) -> Any:
        """Recupera un valor del baúl o avisa si no existe."""
        if key in memory_private_dict:
            return memory_private_dict[key]
        else:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 120, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    # dict store, fn store(key, value)
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
