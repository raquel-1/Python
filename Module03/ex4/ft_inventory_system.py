#!/usr/bin/env python3

import sys


def ft_split(s: str) -> list[str]:
    words = []
    i = 0
    while i < len(s):
        while i < len(s) and s[i] == ':':
            i += 1
        start = i
        while i < len(s) and s[i] != ':':
            i += 1
        if i > start:
            words += [s[start:i]]
    return words


def parse(args: list[str]) -> dict[str, int]:
    dic = {}
    for param in args:
        if ":" not in param:
            print(f"Error - invalid parameter '{param}'")
            continue
        # Split by :
        my_item = ft_split(param)
        if len(my_item) != 2:
            print(f"Error - invalid parameter '{param}'")
            continue
        # separate key : value
        my_key, my_value = my_item
        # Not repeated key
        if my_key in dic:
            print(f"Redundant item '{my_key}' - discarding")
            continue
        # Str to int in exception
        try:
            n_value = int(my_value)
        except ValueError as e:
            print(f"Quantity error for '{my_key}': {e}")
            continue
        # Add to dic
        dic[my_key] = n_value
    return dic


def analyze(inv: dict[str, int]) -> None:
    if not inv:
        return
    total = sum(inv.values())
    all_keys = list(inv.keys())
    print(f"Got inventory: {inv}")
    print(f"Item list: {all_keys}")
    print(f"Total quantity of the {len(all_keys)} items: {total}")
    # Percentage
    for key in all_keys:
        value = inv[key]
        percent = (value / total) * 100
        print(f"Item {key} represents {percent:.1f}%")
    # Most abundant Least abundant
    most_abun = all_keys[0]
    least_abun = all_keys[0]
    for k in all_keys:
        if inv[k] > inv[most_abun]:
            most_abun = k
        if inv[k] < inv[least_abun]:
            least_abun = k
    print(f"Item most abundant: {most_abun} with quantity {inv[most_abun]}")
    print(f"Item least abundant: {least_abun} with quantity {inv[least_abun]}")


if __name__ == "__main__":
    print("===  Inventory System Analysis ===")
    if len(sys.argv) - 1 == 0:
        print("No arguments provided!")
    else:
        # 1-Parse
        inv = parse(sys.argv[1:])
        # 2-Analyze
        analyze(inv)
        # 3-UPDATE
        inv.update({"magic_item": 1})
        print(f"Updated inventory: {inv}")
