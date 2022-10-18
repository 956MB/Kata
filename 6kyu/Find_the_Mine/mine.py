#!/usr/bin/python3

# Find the Mine!
# https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python

def mineLocation(field):
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == 1:
                return [x, y]

if __name__ == '__main__':
    print(mineLocation([ [1, 0], [0, 0] ]), [0, 0])
    print(mineLocation([ [1, 0, 0], [0, 0, 0], [0, 0, 0] ]), [0, 0])
    print(mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ]), [2, 2])
