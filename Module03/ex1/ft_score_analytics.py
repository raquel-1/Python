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
        sum = 0
        high = 0
        for i in lis:
            try:
                n = input_argv(i)
                sum += n
            except Exception as e:
                print(f"Invalid parameter: '{i}'")
                bad = 1
        if (bad != 0):
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            lis_int = [0] * len(lis)
            for i in range(len(lis)):
                lis_int[i] = input_argv(lis[i])
            print("Scores processed:", lis_int)
            print("Total players:", len(lis))
            print("Total score:", sum)
            print("Average score:", sum / len(lis))
            print("High score:", max(lis_int))
            print("Low score:", min(lis_int))
            print("Score range:", max(lis_int) - min(lis_int))
