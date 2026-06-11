#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int]:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Focus"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"}
    ]
    sorted_arts = artifact_sorter(artifacts)
    art0_info = f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power)"
    art1_info = f"{sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)"
    print(f"{art0_info} comes before {art1_info}\n")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\n\n-------------------------------------------------\n")

    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Focus"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"},
        {"name": "Ancient Robe", "power": 40, "type": "Armor"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    art0_info = f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power)"
    art1_info = f"{sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)"
    print(f"{art0_info} comes before {art1_info}\n")

    print("Testing power filter...")
    mages = [
        {"name": "Sebas", "power": 85, "element": "Fire"},
        {"name": "Rachel", "power": 120, "element": "Water"},
        {"name": "Celia", "power": 30, "element": "Earth"}
    ]
    filtered_mages = power_filter(mages, 85)
    for m in filtered_mages:
        print(f"  -> Mage {m['name']} passed with {m['power']} power!")
    print()

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed) + "\n")

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"  Stats calculated: {stats}")
    print(f"  Max Power Level: {stats['max_power']}")
    print(f"  Min Power Level: {stats['min_power']}")
    print(f"  Average Power:   {stats['avg_power']}")
