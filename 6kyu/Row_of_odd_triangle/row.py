#!/usr/bin/python3

# Row of the odd triangle
# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5/train/python

def odd_row2(n):
    # brute force ish count every two numbers n times, append to arr along the way
    # doesnt work great for really large n (times out at 12000ms in large n tests)
    num, arr = 1, [1]

    for i in range(1, n):
        for _ in range(i+1):
            num += 2
            arr.append(num)

    return arr[-n:]

def odd_row1(n):
    # addition method where you count the "outer" number of each n iterations
    # better because we are not strictly adding + 2 and appending to arr every time, probably more efficient, but still times out
    if n == 1: return [1]                   #          1
                                            #        3  (5)  >> 1 + (4) >> 4 + 2 = (6)
    num, arr = 4, []                        #      7   9 (11)  >> 5 + (6) >> 6 + 2 = (8)
    last = num + 1                          #   13  15  17 (19)  >> 11 + (8) >> 8 + 2 = (10)
                                            # 21  23  25  27 (29)  >> etc..
    for _ in range(n-2):
        num += 2
        last += num

    for _ in range(n):
        arr.insert(0, last)
        last -= 2

    return arr

def odd_row(n):
    if n == 1: return [1]
    last = n**2 + n - 1
    begin = last - n*2 + 2
    return list(range(begin, last+1, 2))

if __name__ == '__main__':
    print(odd_row(1), [1])
    print(odd_row(2), [3, 5])
    print(odd_row(3), [7, 9, 11])
    print(odd_row(13), [157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181])
    print(odd_row2(102))
