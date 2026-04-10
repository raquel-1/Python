#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if len(sys.argv) - 1 == 0:
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print("Total arguments:", len(sys.argv))
