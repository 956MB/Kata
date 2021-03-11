#!/usr/bin/env python3

# Return substring instance count - 2
# https://www.codewars.com/kata/52190daefe9c702a460003dd/train/python

def search_substr(full_text, search_text, allow_overlap=True):
    if (full_text == '' or search_text == ''): return 0
    if (not allow_overlap):
        return full_text.count(search_text)
    else:
        i = out = 0
        while True:
            i = full_text.find(search_text, i) + 1
            if i > 0: out += 1
            else: return out

if __name__ == '__main__':
    print("Basic tests")
    print("Should handle matches the simple way")
    print(search_substr('aa_bb_cc_dd_bb_e', 'bb'), 2)
    print(search_substr('aaabbbcccc', 'bbb'), 1)
    print(search_substr('aaacccbbbcccc', 'cc'), 5)
    print(search_substr('aaa', 'aa'), 2)
    print("Should handle non-overlapping cases")
    print(search_substr('aaa', 'aa',False), 1)
    print(search_substr('aaabbbaaa', 'bb',False), 1)
    print("Should handle empty strings on both sides")
    print(search_substr('a', ''), 0)
    print(search_substr('', 'a'), 0)
    print(search_substr('', ''), 0)
    print(search_substr('', '',False), 0)