#!/usr/bin/env python3

# Gap in Primes
# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def check_primes(s,e):
    r = list(range(s+1,e))
    for i in r:
        if is_prime(i): return False
    return True

def gap(g,m,n):
    for i in range(m, n):
        if is_prime(i) and is_prime(i+g):
            valid = check_primes(i, i+g)
            if not valid: continue
            return [i, i+g]
    return None

if __name__ == '__main__':
    print(gap(2,100,110), [101, 103])
    print(gap(4,100,110), [103, 107])
    print(gap(6,100,110), None)
    print(gap(8,300,400), [359, 367])
    print(gap(10,300,400), [337, 347])
