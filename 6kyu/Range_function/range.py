#!/usr/bin/python3

# Range function
# https://www.codewars.com/kata/584ebd7a044a1520f20000d5/train/python

def range_function(*args):
    if len(args) == 1: return range(1, args[0]+1)
    elif len(args) == 2: return range(args[0], args[1]+1)
    elif len(args) == 3: return range(args[0], args[2]+1, args[1])

if __name__ == '__main__':
    print(list(range_function(5)), [1,2,3,4,5], "Expected [1,2,3,4,5]")
    print(list(range_function(3, 7)), [3,4,5,6,7], "Expected [3,4,5,6,7]")
    print(list(range_function(2, 3, 15)), [2,5,8,11,14], "Expected [2,5,8,11,14]")
