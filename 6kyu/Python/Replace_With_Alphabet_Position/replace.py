#!/usr/bin/env python3

# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.find(i)+1) for i in text.lower() if i.isalpha())

if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."), "\n20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    print(alphabet_position("The narwhal bacons at midnight."), "\n20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
