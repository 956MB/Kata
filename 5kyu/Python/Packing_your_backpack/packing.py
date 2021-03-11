#!/usr/bin/python3

# Packing your backpack
# https://www.codewars.com/kata/5a51717fa7ca4d133f001fdf/train/python

from itertools import chain, combinations
 
def pack_bagpack(scores, weights, capacity):
    print(f'Scores: {scores}, Weights: {weights}, Capacity: {capacity}')
    out = []

    for s in range(0, len(scores)-2):
        start = scores[s]
        for w in range(len(weights)-1, 2, -1):
            end = scores[w]
            sec = scores[w-1]
            print([start, sec, end])


def pack_bagpack1(scores, weights, capacity):
    powerset = chain.from_iterable((combinations(weights, i) for i in range(len(weights)+1)))
    # return list(powerset)
    # print(len(list(powerset)))
    matches = list(filter(lambda v: sum(v) <= capacity, powerset))
    print(matches)
    summed = [scores[weights.index(i)] for i in matches[-1]]
    print(summed)
    return sum(summed)


if __name__ == "__main__":
    # print(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8), 29)
    # print(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10), 60)
    print(pack_bagpack([100,5,16,18,50], [25,1,3,2,15], 14), 39)
