#!/usr/bin/python3

# Calculate number of inversions in array
# https://www.codewars.com/kata/537529f42993de0e0b00181f/train/python

def count_inversions(array):
    out = 0

    for n in range(0, len(array)-1):
        current = array[n]
        for x in range(n+1, len(array)):
            if array[x] < current:
                out += 1

    return out


if __name__ == '__main__':
    print(count_inversions([]), 0)
    print(count_inversions([1,2,3]), 0)
    print(count_inversions([2,1,3]), 1)
    print(count_inversions([6,5,4,3,2,1]), 15)
    print(count_inversions([6,5,4,3,3,3,3,2,1]), 30)
