#!/usr/bin/env python3

# Reverse or rotate?
# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

def revrot(string, sz):
    if len(string) == 0 or sz <= 0 or sz > len(string):
        return ""

    chunks = [string[i:i+sz] for i in range(0, len(string), sz)]

    if len(chunks[-1]) < sz:
        chunks = chunks[:-1]

    for i,v in enumerate(chunks):
        ret = 0
        for x in v:
            ret += int(x)**3

        if (ret % 2) == 0:
            chunks[i] = v[::-1]
        else:
            chunks[i] = v[1:] + v[0:1]

    return ''.join(chunks)

if __name__ == '__main__':
    print(revrot("1234", 0), "")
    print(revrot("", 0), "")
    print(revrot("1234", 5), "")
    print(revrot("733049910872815764", 5), "330479108928157")
