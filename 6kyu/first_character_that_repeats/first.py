#!/usr/bin/env python3
# first character that repeats
# https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/train/python
from collections import Counter

def first_dup(s):
    d = Counter(s)
    for k,v in d.items():
        if v >= 2: return k
    return None

if __name__ == '__main__':
    print(first_dup('tweet'), 't')
    print(first_dup('Ode to Joy'), ' ')
    print(first_dup('ode to joy'), 'o')
    print(first_dup('bar'), None)
    print(first_dup('123123'), '1');
    print(first_dup('!@#$!@#$'), '!');
    print(first_dup('1a2b3a3c'), 'a');
