#!/usr/bin/env python3

# The maximum and minimum difference -- Simple version
# https://www.codewars.com/kata/583c5469977933319f000403

# Given arr1 = [3,10,5], arr2 = [20,7,15,8]
# should return [17,2] because 20 - 3 = 17, 10 - 8 = 2

def max_and_min(arr1,arr2):
    _max, _min = 0, 0
    for i1, v1 in enumerate(arr1):
        for i2, v2 in enumerate(arr2):
            diff = abs(v1 - v2)
            if _max == 0: _max = diff
            if _min == 0: _min = diff
            if diff >= _max: _max = diff
            if diff <= _min: _min = diff

    print([_max, _min])
    return [_max, _min]


if __name__ == '__main__':
    print(max_and_min([3,10,5],[20,7,15,8]) == [17,2])
    print(max_and_min([3],[20]) == [17,17])
    print(max_and_min([3,10,5],[3,10,5]) == [7,0])
    print(max_and_min([1,2,3,4,5],[6,7,8,9,10]) == [9,1])