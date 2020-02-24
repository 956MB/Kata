#!/usr/bin/env python3

# Playing with digits
# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    k, total = 1, 0

    for i in list(str(n)):
        total += int(i)**p
        p += 1

    for i in range(1, total):
        mult = n*i
        if mult == total:
            return i
        elif mult > total:
            break

    return -1

if __name__ == '__main__':
    print(dig_pow(89, 1), 1)
    print(dig_pow(92, 1), -1)
    print(dig_pow(46288, 3), 51)
