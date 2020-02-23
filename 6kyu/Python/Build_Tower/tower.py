#!/usr/bin/env python3

# Build Tower
# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    floor = 1
    out = []

    for i in range(n_floors, 0, -1):
        out.append(f'{" " * int(i-1)}{"*"*floor}{" " * int(i-1)}')
        floor += 2

    return out

if __name__ == "__main__":
    print(tower_builder(1))
    print(tower_builder(2))
    print(tower_builder(3))
    print(tower_builder(6))
