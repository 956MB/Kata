#!/usr/bin/env python3

# Beeramid
# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

def beeramid(bonus, price):
    if bonus > 0:
        c, m = 0, 0
        while m <= bonus:
            c += 1
            m += (c**2) * price
        return c-1
    return 0

if __name__ == '__main__':
    print(beeramid(9, 2),  1)
    print(beeramid(21, 1.5),  3)
    print(beeramid(-1, 4), 0)