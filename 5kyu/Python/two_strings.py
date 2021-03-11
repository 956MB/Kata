#!/usr/bin/env python3

# Play with two Strings
# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python

def work_on_strings(a,b):
    outA, outB = a, b

    for _a in outA:
        temp = ""
        for _b in outB:
            temp = temp + _b.swapcase() if (_a.lower() == _b.lower()) else temp + _b
        outB = temp

    for _b in outB:
        temp = ""
        for _a in outA:
            temp = temp + _a.swapcase() if (_a.lower() == _b.lower()) else temp + _a
        outA = temp

    return f"{outA}{outB}"
    
if __name__ == '__main__':
    print(work_on_strings("abc","cde") == "abCCde")
    print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe") == "abcDeFGtrzWDEFGgGFhjkWqE")
    print(work_on_strings("abcdeFg", "defgG") == "abcDEfgDEFGg")
    print(work_on_strings("abab", "bababa") == "ABABbababa")