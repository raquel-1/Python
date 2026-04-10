#!/usr/bin/env python3

import sys

def input_argv(stri: str) -> int:
    return int(stri)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) - 1 == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        lis = sys.argv[1:]
        bad = 0
        for i in lis:
            try:
                input_argv(i)
            except Exception as e:
                print(f"Invalid parameter: '{i}'")
                bad = 1
        if (bad != 0):
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

