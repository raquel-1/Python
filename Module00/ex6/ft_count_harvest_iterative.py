#!/usr/bin/env python3

def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    my_range = range(1, days + 1)
    for i in my_range:
        print(f"Day {i}")
    print("Harvest time!")
