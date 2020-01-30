#!/usr/bin/python3

# Cat and Mouse - Harder Version
# https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf/train/python

def cat_mouse(x, j):
    if not all(i in x for i in ['C', 'D', 'm']):
        return "boring without all three"

    cat = x.index('C')
    dog = False
    for i in x:
        if i == 'm':
            end = cat - j - 2
            step = -1
            break
        elif i == 'C':
            end = cat + j + 2
            step = 1
            break

    # print(cat)
    # print(end)
    for z in range(cat, end, step):
        # print(x[z])
        if x[z] == 'D':
            dog = True
        elif x[z] == 'm':
            if dog:
                return 'Protected!'
            return 'Caught!'
        elif z == end:
            break

    # print(x.index(x[z]))
    return 'Escaped!'


if __name__ == "__main__":
    print(cat_mouse('D..C.......m..........', 7))
    print(cat_mouse('..D.....C.m', 2))
    print(cat_mouse('............C.............D..m...', 8))
    print(cat_mouse('m.C...', 5))
    print(cat_mouse('.CD......m.', 10))
    print(cat_mouse('.CD......m.', 1))
    print(cat_mouse('...m....D....C.......', 10))
