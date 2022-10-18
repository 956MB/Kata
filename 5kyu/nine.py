#!/usr/bin/env python3

# count '9's from 1 to n
# https://www.codewars.com/kata/55143152820d22cdf00001bb/train/python

def count_nines(n):
    return sum([str(x).count('9') for x in range(1, n+1)])

if __name__ == '__main__':
    print(count_nines(1) == 0)
    print(count_nines(9) == 1)
    print(count_nines(100) == 20)
    print(count_nines(200) == 40)
    print(count_nines(201) == 40)
    print(count_nines(278) == 47)
    print(count_nines(279) == 48)
    print(count_nines(280) == 48)
    print(count_nines(908) == 189)
    print(count_nines(909) == 191)
    print(count_nines(99999) == 50000)
    print(count_nines(565754) == 275645)