#!/usr/bin/env python3

# Backwards Read Primes
# https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python

def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def backwards_prime(start, stop):
    arr, res = list(range(start, stop+1)), []
    primes = [int(str(x)[::-1]) for x in arr if int(str(x)[::-1]) != x and is_prime(x)]
    for i in primes:
        if is_prime(i): res.append(int(str(i)[::-1]))
    return res

if __name__ == '__main__':
    a1 = [7027, 7043, 7057]
    print(backwards_prime(7000, 7100), a1)
    a8 = []
    print(backwards_prime(400, 503), a8)
