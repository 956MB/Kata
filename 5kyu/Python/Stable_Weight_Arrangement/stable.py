#!/usr/bin/python3

# Stable Weight Arrangement
# https://www.codewars.com/kata/5d6eef37f257f8001c886d97/train/python

# from itertools import permutations
from random import sample

def solver(arr, n, q):
    arr = list(arr)

# completely random (inefficient) "shuffle" method:
def solver2(arr, n, q):
    arr = list(arr)
    print(f'Initial arr: {arr} n: {n} q: {q}')
    answer, _iter = 1, 0

    while True:
        new_arr = sample(arr, len(arr))
        _iter += 1
        # print('Shuffled:', new_arr)

        # here originally i was checking if a sample was already deemed wrong (in the wrong list).
        # this doesnt make sense, because why check through thousands of wrong answers to see if its already in there.
        # its more efficient to just validate it again because the number of duplicate shuffles is so much lower than the total amount of wrong answers.

        for i in range(0, len(new_arr)-n+1):
            section = new_arr[i:i+n]
            # print('Section:', section, sum(section))
            if sum(section) > q:
                answer = 0
                break

        if answer == 1:
            print(f'Wrong/Iterations: {_iter}')
            return f'Match: {new_arr}'
        elif answer == 0:
            answer = 1

    print(_iter)
    return -1


# preemptive permutation generating method (really struggles over 8 len):
def solver1(arr, n, q):
    print(f'Initial arr: {arr} n: {n} q: {q}')
    _all = permutations(arr)
    _all_list = list(_all)
    answer, matches = 1, []
    # print('First:', _all_list[0])
    print(len(_all_list))
    # return list(reversed(_all_list))[0]
    _all_list = list(reversed(_all_list))

    for _list in _all_list:
        num = _all_list.index(_list)
        for i in range(0, len(_list)-n+1):
            section = _list[i:i+n]
            if sum(section) > q:
                answer = 0
                break
            print(new_arr)
            # print('Section:', section, sum(section))

        if answer == 1:
            return f'Match: {_list} Index: {num}'
            # matches.append(_list)
        elif answer == 0:
            answer = 1

    # if len(matches) > 0:
        # return f'Match: {matches[-1]}'
        # for match in matches:
            # print(match)
        # return 'done'
    return -1

    # return itertools.chain.from_iterable((itertools.combinations(arr, i) for i in range(len(arr)+1)))
    # return type(arr)

if __name__ == "__main__":
    print(solver((3,5,7,1,6,8,2,4),3,13), '\n')
    # print(solver((7,12,6,10,3,8,5,4,13,2,9),4,28), '\n')
    # print(solver((9,16,11,6,15,14,19,3,12,18,7),3,35), '\n')
    # print(solver((33,34,29,25,36,30,27,32,21,35,39),5,155), '\n')
    # print(solver((22,14,30,25,29,19,21,17,15,32,20),4,92), '\n')
    # print(solver((3,5,7,1,6),3,13), '\n')
