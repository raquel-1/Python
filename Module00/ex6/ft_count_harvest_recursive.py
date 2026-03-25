#!/usr/bin/env python3

def recursive_mine(days: int) -> None:
    if days >= 2:
        recursive_mine(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    recursive_mine(days)
    print("Harvest time!")
