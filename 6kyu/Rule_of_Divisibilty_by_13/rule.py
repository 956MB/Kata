#!/usr/bin/env python3

# A Rule of Divisibility by 13
# https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python

def thirt(n):
    powers = [1, 10, 9, 12, 3, 4]
    s, x, add = list(str(n)), 0, 0
    
    while len(s) > 2:
        for i in range(len(s), 0, -1):
            add += int(s[i-1]) * powers[x % 6)]
            x += 1
        s, x, add = list(str(add)), 0, 0

    return int(''.join(s))

if __name__ == '__main__':
    print(thirt(8529), 79)
    print(thirt(85299258), 31)
    print(thirt(5634), 57)
    print(thirt(1111111111), 71)
    print(thirt(987654321), 30)
