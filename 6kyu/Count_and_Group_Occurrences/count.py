#!/usr/bin/env python3

# Count and Group Character Occurrences in a String
# https://www.codewars.com/kata/543e8390386034b63b001f31/train/python

def get_char_count(s):
    s = [c.lower() for c in s if c.isalpha() or c.isdigit()]
    d, out = {}, {}

    for c in s:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1

    for i in set(d.values()):
        out[i] = sorted([l for l in d.keys() if d[l] == i])

    return {k: v for k, v in sorted(out.items(), key=lambda x: x[0], reverse=True)}

if __name__ == '__main__':
    print(get_char_count("Mississippi"), {4: ["i", "s"], 2: ["p"], 1: ["m"]})
    print(get_char_count("Hello. Hello? HELLO!"), {6: ["l"], 3: ["e", "h", "o"]})
    print(get_char_count("aaa...bb...c!"), {3: ["a"], 2: ["b"], 1: ["c"]})
    print(get_char_count("abc123"), {1: ["1", "2", "3", "a", "b", "c"]})
    print(get_char_count("aaabbbccc"), {3: ["a", "b", "c"]})
