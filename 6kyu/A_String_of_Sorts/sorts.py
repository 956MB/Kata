#!/usr/bin/env python3
# A String of Sorts
# https://www.codewars.com/kata/536c6b8749aa8b3c2600029a/train/python

def sort_string(s, ordering):
    s, ordering, out = list(s), list(ordering), ''
    for i in ordering:
        let = [x for x in s if x == i]
        s = [e for e in s if e != i]
        out += ''.join(let)
    out += ''.join(s)
    return out

if __name__ == '__main__':
    print(sort_string("foos", "of"), "oofs")
    print(sort_string("string", "gnirts"), "gnirts")
    print(sort_string("banana", "a"), "aaabnn")
