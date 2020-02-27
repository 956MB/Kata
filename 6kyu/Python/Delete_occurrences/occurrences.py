#!/usr/bin/env python3

# Delete occurrences of an element if it occurs more than n times
# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order, max_e):
    out = []

    for i in order:
        if out.count(i) < max_e:
            out.append(i)

    return out

if __name__ == '__main__':
    print(delete_nth([20,37,20,21], 1), [20,37,21])
    print(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
