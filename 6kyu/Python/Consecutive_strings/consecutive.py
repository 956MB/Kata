#!/usr/bin/env python3

# Consecutive strings
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    out = ""

    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr)-k+1):
            word = ''.join([strarr[j] for j in range(i, k+i)])
            if len(word) > len(out):
                out = word

    return out

if __name__ == '__main__':
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    print(longest_consec([], 3), "")
    print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
    print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
    print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
