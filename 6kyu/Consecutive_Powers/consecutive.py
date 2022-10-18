#!/usr/bin/python3

# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b):
    store, out = [], []
    for i in range(a, b+1):
        # print(f'I: {i}')
        for n in range(1, len(str(i))+1):
            num = int(str(i)[n-1])
            calc = num**n
            # print(f'Num: {num}, Calc: {calc}')
            store.append(calc)

        # print(f'Store: {store}\n')
        if sum(store) == i:
            out.append(i)
        store = []

    return out

if __name__ == '__main__':
    print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
    print(sum_dig_pow(10, 89),  [89])
    print(sum_dig_pow(10, 100),  [89])
    print(sum_dig_pow(90, 100), [])
    print(sum_dig_pow(89, 135), [89, 135])
