#!/usr/bin/python3

# Largest Number Arrangement
# https://www.codewars.com/kata/59d902f627ee004281000160/train/python

def parse(data):
    num = 0
    out = []
    for i in list(data):
        if i in 'i':
            num += 1
        elif i in 'd':
            num -= 1
        elif i in 's':
            num = num**2
        elif i in 'o':
            out.append(num)

    return out

if __name__ == '__main__':
    print(parse("ooo"), [0,0,0])
    print(parse("ioioio"), [1,2,3])
    print(parse("idoiido"), [0,1])
    print(parse("isoisoiso"), [1,4,25])
    print(parse("codewars"), [0])
