#!/usr/bin/env python3

import sys

def input_argv(stri: str) -> int:
    return int(stri)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    lis = sys.argv[1:]
    lis_int = []
    bad = 0
    sum = 0
    high = 0
    for i in lis:
        try:
            n = input_argv(i)
            lis_int += [n]
            sum += n
        except Exception as e:
            print(f"Invalid parameter: '{i}'")
            # bad = 1
    if len(lis_int) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed:", lis_int)
        print("Total players:", len(lis))
        print("Total score:", sum)
        print("Average score:", sum / len(lis))
        print("High score:", max(lis_int))
        print("Low score:", min(lis_int))
        print("Score range:", max(lis_int) - min(lis_int))
