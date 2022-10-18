#!/usr/bin/env python3

# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(i) == 1 else ")" for i in word.lower()])

if __name__ == '__main__':
    print(duplicate_encode("din"),"(((")
    print(duplicate_encode("recede"),"()()()")
    print(duplicate_encode("Success"),")())())","should ignore case")
    print(duplicate_encode("(( @"),"))((")
