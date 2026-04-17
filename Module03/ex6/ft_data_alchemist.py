#!/usr/bin/env python3

import random

players = [
    'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
    'Gregory', 'john', 'kevin', 'Liam'
    ]

# new list with all names capitalized
all_capi = [name.capitalize() for name in players]
# new list with only capitalized names
only_capi = [name for name in players if name.capitalize() == name]
# dictionary with keys = capitalized_list values = random_scores
dic = {name: random.randint(0, 1000) for name in all_capi}
average = sum(dic.values()) / len(dic.keys())
# dictionary containing only scores above the average
dic_average = {name: dic[name] for name in dic if dic[name] > average}

if __name__ == "__main__":
    print("===  Game Data Alchemist ===")
    print("Initial list of players:", players)
    print("New list with all names capitalized:", all_capi)
    print("New list of capitalized names only:", only_capi)
    print("Score dict:", dic)
    print(f"Score average is {average:.2f}")
    print("High scores:", dic_average)
