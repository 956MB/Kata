#!/usr/bin/env python3

# Numericals of a String
# https://www.codewars.com/kata/5b4070144d7d8bbfe7000001/train/python

def numericals(s):
    d, out = {}, ""

    for i in s:
        if not i in d:
            d[i] = 1
            out += "1"
        else:
            d[i] += 1
            out += str(d[i])

    return out

    # works but the count for long strings times out in test cases:
    # return ''.join([str(s[:i+1].count(s[i])) for i in range(len(s))])

if __name__ == '__main__':
    print(numericals("Hello, World!"), "1112111121311")
    print(numericals("Hello, World! It's me, JomoPipi!"), "11121111213112111131224132411122")
    print(numericals("hello hello"), "11121122342")
    print(numericals("Hello"), "11121")
    print(numericals("aaaaaaaaaaaa"),"123456789101112")
