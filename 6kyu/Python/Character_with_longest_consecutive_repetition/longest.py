#!/usr/bin/env python3

# Character with longest consecutive repetition
# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

from itertools import groupby

def longest_repetition(chars):
    if chars == "": return ('', 0)
    group = [''.join(g) for _,g in groupby(chars)]
    _max = max(group, key=len)
    return (_max[0], len(_max))

if __name__ == '__main__':
    print(longest_repetition("aaaabb"), ('a', 4))
    print(longest_repetition("bbbaaabaaaa"), ('a', 4))
    print(longest_repetition("cbdeuuu900"), ('u', 3))
    print(longest_repetition("abbbbb"), ('b', 5))
    print(longest_repetition("aabb"), ('a', 2))
    print(longest_repetition("ba"), ('b', 1))
    print(longest_repetition(""), ('', 0))
