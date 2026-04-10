#!/usr/bin/env python3

import sys


def input_argv(stri: str) -> int:
    return int(stri)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    lis = sys.argv[1:]
    lis_int = []
    high = 0
    for i in lis:
        try:
            n = input_argv(i)
            lis_int += [n]
        except Exception:
            print(f"Invalid parameter: '{i}'")
    if len(lis_int) == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print("Scores processed:", lis_int)
        print("Total players:", len(lis))
        print("Total score:", sum(lis_int))
        print("Average score:", sum(lis_int) / len(lis_int))
        print("High score:", max(lis_int))
        print("Low score:", min(lis_int))
        print("Score range:", max(lis_int) - min(lis_int))
