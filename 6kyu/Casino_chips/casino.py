#!/usr/bin/python3

# Casino chips
# https://www.codewars.com/kata/5e0b72d2d772160011133654/train/python

def solve(arr):
    return min(sorted(arr)[0] + sorted(arr)[1], sum(arr) // 2)

if __name__ == '__main__':
    print(solve([1,1,1]), 1)
    print(solve([1,2,1]), 2)
    print(solve([4,1,1]), 2)
    print(solve([8,2,8]), 9)
    print(solve([8,1,4]), 5)
    print(solve([7,4,10]), 10)
    print(solve([12,12,12]), 18)
    print(solve([1,23,2]), 3)
