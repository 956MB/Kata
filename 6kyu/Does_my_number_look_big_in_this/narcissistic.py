#!/usr/bin/python3

# Does my number look big in this?
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic(value):
    return sum([int(x)**len(str(value)) for x in str(value)]) == value

if __name__ == '__main__':
    print(narcissistic(7), True, '7 is narcissistic');
    print(narcissistic(371), True, '371 is narcissistic');
    print(narcissistic(122), False, '122 is not narcissistic')
    print(narcissistic(4887), False, '4887 is not narcissistic')
