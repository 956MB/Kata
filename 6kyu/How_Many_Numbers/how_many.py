#!/usr/bin/python3

# How Many Numbers?
# https://www.codewars.com/kata/55d8aa568dec9fb9e200004a/train/python

def sel_number(n, d):
    out, match = 0, True

    for num in range(12, n+1):
        for n in range(0, len(str(num))-1):
            _1 = int(str(num)[n])
            _2 = int(str(num)[n+1])
            if 1 <= _2 - _1 <= d:
                pass
            else:
                match = False
                break

        if match:
            out += 1
        else:
            match = True

    return out

if __name__ == '__main__':
    print(sel_number(0, 1), 0 )
    print(sel_number(3, 1), 0)
    print(sel_number(13, 1), 1)
    print(sel_number(15, 1), 1)
    print(sel_number(20, 2), 2)
    print(sel_number(47, 3), 12)
    print(sel_number(62285, 9), 372)
