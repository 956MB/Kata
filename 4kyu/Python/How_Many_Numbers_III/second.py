#!/usr/bin/python3

# How many numbers III?
# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    matches = [''.join(str(i) for i in list(c)) for c in combs if sum(c) == sum_dig]

    if not matches:
        return []
    return [len(matches), int(matches[0]), int(matches[-1])]


if __name__ == '__main__':
    # print(find_all(10, 3), [8, 118, 334])
    # print(find_all(27, 3), [1, 999, 999])
    # print(find_all(84, 4), [])
    # print(find_all(35, 6), [123, 116999, 566666])
    print(find_all(85, 17), ['??'])
    # print(find_all(105, 17), ['??'])
