#!/usr/bin/env python3

import math


Point3D = tuple[float, float, float]


def distance(c1: Point3D, c2: Point3D) -> float:
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def ft_split(s: str) -> list:
    words = []
    i = 0
    while i < len(s):
        while i < len(s) and s[i] == ',':
            i += 1
        start = i
        while i < len(s) and s[i] != ',':
            i += 1
        if i > start:
            words += [s[start:i]]
    return words


def ft_trim(s: str) -> str:
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    j = len(s) - 1
    while j >= 0 and s[j] == ' ':
        j -= 1
    return s[i:j+1]


def format(s: str) -> Point3D:
    parts = ft_split(s)
    coords = []
    if len(parts) != 3:
        print("Invalid syntax")
        return
    for part in parts:
        trimmed = ft_trim(part)
        try:
            coords += [float(trimmed)]
        except ValueError as e:
            print(f"Error on parameter '{trimmed}': {e}")
            return
    return (coords[0], coords[1], coords[2])


def get_player_pos():
    while True:
        s = input("Enter new coordinates as floats in format 'x,y,z': ")
        coor = format(s)
        if coor is not None:
            x, y, z = coor
            print(f"Got a first tuple: {coor}")
            print(f"It includes: X={x}, Y={y}, Z={z}")
            break
    return coor

if __name__ == "__main__":
    print("Get a first set of coordinates")
    c1 = get_player_pos()
    print("Distance to center:", round(distance(c1, (0, 0, 0)), 4))
    print("")
    print("Get a second set of coordinates")
    c2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:", round(distance(c1, c2), 4))
