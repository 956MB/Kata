#!/usr/bin/python3

# Next bigger number with the same digits
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

# Definitely not the most efficient, but it works.
# I had to basically touch and go with the amount of loops to get the test case numbers to work, not the best way to do that... idk...

def next_smaller(n):
    start = sorted(str(n))
    while n > 0 and len(str(n)) == len(start):
        n -= 1
        if start == sorted(str(n)):
            return n

    return -1

if __name__ == "__main__":
    # print(next_smaller(907), 790)
    # print(next_smaller(531), 513)
    # print(next_smaller(135), -1)
    # print(next_smaller(2071), 2017)
    # print(next_smaller(414), 144)
    # print(next_smaller(123456798), 123456789)
    print(next_smaller(123456789), -1)
    # print(next_smaller(100000009), -1)
    # print(next_smaller(1234567908), 1234567890)
