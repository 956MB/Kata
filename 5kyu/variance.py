#!/usr/bin/env python3

# Calculate Variance
# https://www.codewars.com/kata/5266fba01283974e720000fa/train/python

# mean = (1 + 2 + 2 + 3) / 4
# => 2

# variance = ((1 - 2)^2 + (2 - 2)^2 + (2-2)^2 + (3 - 2)^2)  /  4
# => 0.5

def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum([(x - mean)**2 for x in numbers]) / len(numbers)

if __name__ == '__main__':
    print(variance([-10, 0, 10, 20, 30]) == 200)
    print(variance([8, 9, 10, 11, 12]) == 2)
    print(variance([1.5, 2.5, 4, 2, 1, 1]) == 1.0833333333333333)