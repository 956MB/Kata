#!/usr/bin/python3

def max_sequence(arr):
    num = 0

    for x in range(len(arr) + 1):
        for y in range(x + 1, len(arr) + 1):
            if sum(arr[x:y]) > num:
                num = sum(arr[x:y])

    return num

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))