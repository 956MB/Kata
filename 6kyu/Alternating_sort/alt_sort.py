#!/usr/bin/env python3
# Alternating Sort
# https://www.codewars.com/kata/5ac49156376b11767f00060c/train/python
from itertools import chain, zip_longest

def alternate_sort(l):
    # print(f'start: {l}')
    p = sorted([i for i in l if i >= 0])
    n = sorted([i for i in l if i < 0], reverse=True)
    # print(f'p: {p}, n: {n}')

    ret = list(chain.from_iterable(zip_longest(n,p)))
    # print(ret)
    return [i for i in ret if i is not None]

if __name__ == '__main__':
    print(alternate_sort([5, 2, -3, -9, -4, 8,]), [-3, 2, -4, 5, -9, 8], "Test for even array length")
    print(alternate_sort([5, -42, 2, -3, -4, 8, 9]), [-3, 2, -4, 5, -42, 8, 9], "Test for uneven array length")
    print(alternate_sort([5, -42, 8, 2, -3, -4, 9]), [-3, 2, -4, 5, -42, 8, 9], "Test for uneven array length with additional positive integers")
    print(alternate_sort([5, -42, -8, 2, -3, -4, -9]), [-3, 2, -4, 5, -8, -9, -42], "Test for uneven array length with additional negative integers")
    print(alternate_sort([5, 2, 3, 4, 8, 9]), [2, 3, 4, 5, 8, 9], "Test for array with only positive integers")
    print(alternate_sort([-5, -2, -3, -4, -8, -9]), [-2, -3, -4, -5, -8, -9], "Test for array with only negative integers")
    print(alternate_sort([-5, -2, 3, 4, -8, 0, -9]), [-2, 0, -5, 3, -8, 4, -9], "Test for array with 0")
    print(alternate_sort([-5, -2, 3, 9, 4, -2,-8, 0, 9, -9]), [-2, 0, -2, 3, -5, 4, -8, 9, -9, 9], "Test for array with 0")
