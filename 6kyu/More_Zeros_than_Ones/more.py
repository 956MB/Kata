#!/usr/bin/env python3

# More Zeros than Ones
# https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python

from collections import OrderedDict

def more_zeros(s):
    return [x for x in OrderedDict((l, True) for l in s).keys() if format(ord(x), 'b').count('0') > format(ord(x), 'b').count('1')]

if __name__ == '__main__':
    print(more_zeros('abcde'), ['a', 'b', 'd'])
    print(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
    print(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
    print(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'), ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0'])
    print(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])
