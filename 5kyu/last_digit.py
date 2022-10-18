#!/usr/bin/env python3

# Last digit of a large number
# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

def last_digit(n1, n2):
    return str(n1 ** n2)[-1]

if __name__ == '__main__':
    print(last_digit(4, 1) == 4)
    print(last_digit(4, 2) == 6)
    print(last_digit(9, 7) == 9)
    print(last_digit(10, 10 ** 10) == 0)
    print(last_digit(2 ** 200, 2 ** 300) == 6)
    # print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)