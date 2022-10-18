#!/usr/bin/env python3
# Alternating Loops
# https://www.codewars.com/kata/55e529bf6c6497394a0000b5/train/python
from itertools import chain, zip_longestl

def combine(*args):
    ret = list(itertools.chain.from_iterable(itertools.zip_longest(*args)))
    return [i for i in ret if i is not None]

if __name__ == '__main__':
    print(combine(['a', 'b', 'c'], [1, 2, 3]), ['a', 1, 'b', 2, 'c', 3])
    print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]), ['a', 1, 'b', 2, 'c', 3, 4, 5])
    print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]),['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
    print(combine([{ 'a': 1 }, { 'b': 2 }], [1, 2]),[{"a":1},1,{"b":2},2])
    print(combine([{ 'a': 2, 'b':1 }, { 'a': 1, 'b': 2 }], [1, 2, 3, 4],[5,6],[7]), [{"a":2,"b":1},1,5,7,{"a":1,"b":2},2,6,3,4])
