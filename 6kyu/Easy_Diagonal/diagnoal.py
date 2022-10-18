#!/usr/bin/python3

# Easy Diagonal
# https://www.codewars.com/kata/559b8e46fa060b2c6a0000bf/train/python
import sys

def diagonal(n, p):
    arr = [[1 for _ in range(n+1)],[1]]
    store = 1
    # print(arr[0])
    for x in range(1, p+1):
        for i in range(1, n):
            add = arr[x-1][i] + store
            arr[x].append(add)
            store = add

        arr.append([1])
        store = 1
        n -= 1
        # print(arr[x])
    return sum(arr[-2])

if __name__ == '__main__':
    print(diagonal(20, 4),20349)
    print(diagonal(20, 5), 54264)
    print(diagonal(20, 15), 20349)
    # print(diagonal(int(sys.argv[1]), int(sys.argv[2])))
