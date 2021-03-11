#!/usr/bin/python3

from time import sleep
import sys

def main(arr, n, q):
    arr = list(arr)
    for i in range(0, len(arr)-n+1):
        j = 0
        while True:
            _set = sum(arr[i:i+n])
            if _set > q:
                value = arr.pop(0)
                arr.append(value)
            else:
                break
    return arr

def main2(arr, n, q):
    arr = list(arr)
    count = 0

    for _ in range(500000):
        for i in range(len(arr)-1, 0, -1):
            swapped = swap(arr, arr[0], arr[i])
            arr = swapped[0]
            # print(arr)
            got_match = match(arr, n, q)

            if got_match:
                return f'match found: {arr} {count} iterations'

    return -1

def swap(list, pos1, pos2):
    num1 = list.index(pos1)
    num2 = list.index(pos2)
    list[num1], list[num2] = list[num2], list[num1]
    return [list, pos1, pos2]


def main1(arr, n, q):
    arr = list(arr)
    og = arr
    start, end, count = 0, n, 0
    move = end+n-1

    while True:
        for _ in range(3):
            for _ in range(n):
                arr.insert(move, arr.pop(start))
                got_match = match(arr, n, q)

                if got_match:
                    return f'match found: {arr} {count} iterations'
                # elif arr == og:
                    # print(f'back to og {x+y} iterations')

            # print(arr)
            start += 1
            move += 1
            count += 1

        start = 0
        move = end+n-1

    return -1

def match(arr, n, q):
    answer = 1

    for i in range(0, len(arr)-n+1):
        section = arr[i:i+n]
        if sum(section) > q:
            answer = 0
            break

    if answer == 1:
        return True
    elif answer == 0:
        return False

if __name__ == "__main__":
    arr, n, q = (3,5,7,1,6,8,2,4), 3, 13
    print(list(arr))
    print(main(arr, n, q))
