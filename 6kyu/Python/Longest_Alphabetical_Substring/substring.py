#!/usr/bin/python3

# Longest alphabetical substring
# https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python

def longest(s):
    # print('String:', s)
    out, store = s[0], s[0]
    asci = 'abcdefghijklmnopqrstuvwxyz'
    # print(asci.index(''), asci.index('a'))
    for i in s[1:]:
        if asci.index(i) >= asci.index(store[-1]):
            store += i
            # print('Store:', store)
        elif len(i) == len(store):
            store = i
        elif len(store) > len(out):
            out = store
            # print('Out:', out)
            store = i
        else:
            store = i
    
    if len(store) > len(out): out = store
    return out

if __name__ == '__main__':
    print(longest('asd'))
    print(longest('nab'))
    print(longest('abcdeapbcdef'))
    print(longest('asdfaaaabbbbcttavvfffffdf'))
    print(longest('asdfbyfgiklag'))
    print(longest('z'))
    print(longest('zyba'))
