#!/usr/bin/env python3

import random
from typing import Generator

players = ["alice", "bob", "charlie", "dylan"]
actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (
            players[random.randint(0, len(players) - 1)],
            actions[random.randint(0, len(actions) - 1)]
        )


def consume_event(
    even_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(even_list) > 0:
        n_remov = random.randint(0, len(even_list) - 1)
        retun_ev = even_list[n_remov]
        even_list[:] = even_list[:n_remov] + even_list[n_remov + 1:]
        yield retun_ev


if __name__ == "__main__":
    gen = gen_event()
    # list of 1000 events
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    # list of 10 events
    even_list = []
    for i in range(0, 10):
        even_list += [next(gen)]
    print("Built list of 10 events:", even_list)
    # even_list is updated within consume_event
    for event in consume_event(even_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {even_list}")
