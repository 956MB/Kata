#!/usr/bin/env python3

# Lazy Repeater
# https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3/train/python

class make_looper():
    def __init__(self, string):
        self.str = string
        self.end = len(string)-1
        self.idx = 0

    def __call__(self):
        self.idx = self.idx + 1 if self.idx < self.end else 0
        return self.str[self.idx-1]

if __name__ == '__main__':
    print("Sample Tests")

    abc = make_looper("abc")

    print(abc(), 'a')
    print(abc(), 'b')
    print(abc(), 'c')

    print(abc(), 'a')
    print(abc(), 'b')
    print(abc(), 'c')