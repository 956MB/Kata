#!/usr/bin/python3

# Split and then add both sides of an array together.
# https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/python

def split_and_add(numbers, n):
    out = []
    for i in range(n):
        if len(numbers) == 1:
            return numbers
        left = numbers[:len(numbers)//2]
        right = numbers[len(numbers)//2:]
        # print(left, right)
        while len(left) < len(right): left.insert(0, 0)
        for x in range(len(right)):
            out.append(left[x] + right[x])

        numbers = out
        # print(out)
        out = []

    return numbers

if __name__ == '__main__':
    print(split_and_add([1,2,3,4,5], 2))
    print(split_and_add([1,2,3,4,5], 3))
    print(split_and_add([15], 3))
    print(split_and_add([32,45,43,23,54,23,54,34], 2))
    print(split_and_add([32,45,43,23,54,23,54,34], 0))
    print(split_and_add([3,234,25,345,45,34,234,235,345], 3))
    print(split_and_add([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4))
    print(split_and_add([23,345,345,345,34536,567,568,6,34536,54,7546,456], 20))
