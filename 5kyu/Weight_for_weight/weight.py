#!/usr/bin/env python3

# Weight for weight
# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def order_weight(string):
    # print(f"Start: {string}")
    n, s = [], []

    for i in string.split():
        n.append([i, sum_digits(int(i))])

    # print(f"N:{n}\n")
    n.sort(key=lambda x: x[1])
    # print(f"N sorted:{n}\n")
    sec = sorted(set([li[1] for li in n]))

    for x in sec:
        sep = [li for li in n if li[1] == x]
        s.append(sorted(sep, key=lambda z: z[0]))

    return ' '.join([l0[0] for l1 in s for l0 in l1])

if __name__ == "__main__":
    print(order_weight("103 123 4444 99 2000"), "\n2000 103 123 4444 99")
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "\n11 11 2000 10003 22 123 1234000 44444444 9999")
