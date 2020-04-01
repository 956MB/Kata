#!/usr/bin/env python3
# Password Maker
# https://www.codewars.com/kata/5b3d5ad43da310743c000056/train/python
# this is so dumb, im ashamed
import random, string, re

def make_password(length, flagUpper, flagLower, flagDigit):
    out, rex = '', ['^', '[', '{%d}' % length, '$']
    if flagUpper:
        out += string.ascii_uppercase
        rex.insert(1, '(?=.*?[A-Z])')
        rex[-3] += 'A-Z'
    if flagLower:
        out += string.ascii_lowercase
        rex.insert(1, '(?=.*?[a-z])')
        rex[-3] += 'a-z'
    if flagDigit:
        out += string.digits
        rex.insert(1, '(?=.*?[0-9])')
        rex[-3] += '0-9'
    rex[-3] += ']'
    rex = r''.join(rex)
    ret = ''.join(random.sample(out, length))
    while not bool(re.search(rex, ret)):
        ret = ''.join(random.sample(out, length))
    return ret

if __name__ == '__main__':
    length, flagUpper, flagLower, flagDigit = 5, True, False, False
    print(make_password(length, flagUpper, flagLower, flagDigit))
    length, flagUpper, flagLower, flagDigit = 5, False, True, False
    print(make_password(length, flagUpper, flagLower, flagDigit))
    length, flagUpper, flagLower, flagDigit = 5, False, False, True
    print(make_password(length, flagUpper, flagLower, flagDigit))
    length, flagUpper, flagLower, flagDigit = 5, True, True, False
    print(make_password(length, flagUpper, flagLower, flagDigit))
