#!/usr/bin/python3

# Josephus Survivor
# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python

'''
1 2 3 4 5 6 7 >> init:
1 2 4 5 6 7   >> 3: store: 4, remove: +2 = 6
1 2 4 5 7     >> 6: store: 7, remove: +2 = 2
1 4 5 7       >> 2: store: 4, remove: +2 = 7
1 4 5         >> 7: store: 1, remove: +2 = 5
1 4           >> 5: store: 1, remove: +2 = 1
4             >> Survivor: 4
'''

def josephus_survivor(n,k):
    if n == 1: return 1
    arr, i = list(range(1, n+1)), 0
    print(f'Start: {n,k} {arr}')

    while len(arr) > 1:
        i = (k-1 + i) % len(arr)
        arr.pop(i)

    # return arr[0]}
    return f'Final: {arr[0]}'

    # v = 0
    # for i in range(1, n+1):
        # v = (v + k) % i
    # return v + 1

'''
# some rabbit hole sh** here
def josephus_survivor1(n,k):
    arr = list(range(1, n+1))
    print(f'Start: {arr}')

    start = k - 1
    arr.remove(arr[start])
    start = start - 1
    for i in range(n):
        start = start + n
        arr.remove(arr[start])
        # start = start -

# and here
def josephus_survivor2(n,k):
    arr = list(range(1, n+1))
    print(f'Start: {arr}')

    for _ in range(6):
        mod = len(arr)%k + 1
        _3_more = mod + 2
        # print(_3_more)
        rem = arr[mod]
        arr.remove(rem)
        if _3_more <= len(arr):
            rem2 = arr[_3_more]
            arr.remove(rem2)
            rem = str(rem) + ', ' + str(rem2)
        print(arr, f'Removed: ({rem}) Index: {mod}')

    return arr
'''

if __name__ == "__main__":
    print(josephus_survivor(7,3),4)
    print(josephus_survivor(11,19),10)
    print(josephus_survivor(1,300),1)
    print(josephus_survivor(14,2),13)
    print(josephus_survivor(100,1),100)
