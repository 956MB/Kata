#!/usr/bin/python3

# Largest Number Arrangement
# https://www.codewars.com/kata/59d902f627ee004281000160/train/python

from itertools import permutations

def largest_arrangement(numbers):
    numbers = list(map(str, numbers))
    numbers = permutations(numbers)
    numbers_list = list(numbers)
    return max([int(x) for x in [''.join(n) for n in numbers_list]])

def largest_arrangement1(numbers):
    # creating all the permutations, but looping through them in order and assigning the max along the way
    numbers = permutations(numbers)
    numbers_list = list(numbers)
    out = 0

    for _list in numbers_list:
        string = ""
        for n in _list:
            string += str(n)

        if int(string) > out:
            out = int(string)

    return out

if __name__ == '__main__':
    print(largest_arrangement([8, 6, 590, 70]), 8706590)
    print(largest_arrangement([6, 73, 79, 356, 7]), 797736356)
    print(largest_arrangement([64, 29, 5, 9, 982, 3]), 9982645329)
    print(largest_arrangement([3487, 103559, 243]), 3487243103559)
    print(largest_arrangement([7, 78, 79, 72, 709, 7, 94]), 9479787772709)
