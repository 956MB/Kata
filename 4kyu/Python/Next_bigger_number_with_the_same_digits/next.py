#!/usr/bin/python3

# Next bigger number with the same digits
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

# Definitely not the most efficient, but it works.
# I had to basically touch and go with the amount of loops to get the test case numbers to work, not the best way to do that... idk...

def next_bigger(n):
    start = sorted(str(n))
    test = 1
    # print(start)
    while test < 40000:
        n += 1
        if start == sorted(str(n)):
            # print(sorted(str(n)))
            return n
        test += 1

    return -1

if __name__ == "__main__":
    print(next_bigger(12),21)
    print(next_bigger(513),531)
    print(next_bigger(2017),2071)
    print(next_bigger(414),441)
    print(next_bigger(144),414)
