#!/usr/bin/env python3

# longest_palindrome
# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

def longest_palindrome(s):
    # pretty weird huh, not really a normal/efficient way of finding palindromes, or is it? idk, it works. kinda. sometimes.
    if len(s) == 1: return 1
    elif len(s) == 0: return 0
    left, right, dromes, done = "", "", [], False

    for x in range(0, len(s)-1):
        letter_l = s[x]
        for y in range(len(s)-1, 0, -1):
            if y < x:
                break
            letter_r = s[y]

            if letter_l == letter_r:
                if s[x+1] == s[y-1]:
                    if x == y:
                        left += letter_l
                        done = True
                        break
                    elif s[x] == s[x+1]:
                        done = True

                    left += letter_l
                    right = letter_r + right
                    break

        if done:
            palindrome = left + right
            dromes.append(palindrome)
            left, right = "", ""
            done = False

    if len(dromes) == 0:
        return 1
    return len(sorted(dromes, key=len)[-1])

if __name__ == '__main__':
    print(longest_palindrome("a"), 1)
    print(longest_palindrome("aa"), 2)
    print(longest_palindrome("baa"), 2)
    print(longest_palindrome("aab"), 2)
    print(longest_palindrome("abcdefghba"), 1)
    print(longest_palindrome("baablkj12345432133d"), 9)
