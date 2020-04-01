#!/usr/bin/env python3
# Steps in Primes
# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python

def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def step(g,m,n):
    for i in range(m, n):
        if i+g > n: break
        elif is_prime(i) and is_prime(i+g):
            return [i, i+g]
    return None

if __name__ == '__main__':
    print(step(2,100,110), [101, 103])
    print(step(4,100,110), [103, 107])
    print(step(2,5,5), None)
    print(step(6,100,110), [101, 107])
    print(step(8,300,400), [359, 367])
    print(step(10,300,400), [307, 317])
    print(step(16,5,20), None)
    print(step(6, 94477, 194477), [94477, 94483])
