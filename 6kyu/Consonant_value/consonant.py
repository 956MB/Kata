#!/usr/bin/env python3

# Consonant value
# https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

import re

def solve(s):
    alpha, tot, temp = 'abcdefghijklmnopqrstuvwxyz', 0, 0
    s = ''.join(',' if c in 'aeiou' else c for c in s)
    s = [i for i in s.split(',') if i]
    for i in s:
        for x in list(i):
            temp += alpha.index(x)+1
        tot = temp if temp >= tot else tot
        temp = 0
    return tot

if __name__ == '__main__':
    print(solve("zodiacs"),26)
    print(solve("chruschtschov"),80)
    print(solve("khrushchev"),38)
    print(solve("strength"),57)
    print(solve("catchphrase"),73)
    print(solve("twelfthstreet"),103)
    print(solve("mischtschenkoana"),80)
