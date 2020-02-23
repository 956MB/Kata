#!/usr/bin/env python3

# Closest and Smallest
# https://www.codewars.com/kata/5868b2de442e3fb2bb000119/train/python

def minDistance(lst):
    lst = sorted(lst, key=lambda x: x[0])
    index = -1
    distance = lst[-1][0] - lst[0][0]
    for i in range(len(lst)-1):
        if lst[i+1][0] - lst[i][0] < distance:
            distance = lst[i+1][0] - lst[i][0]
            index = i
    for i in range(len(lst)-1):
        if lst[i+1][0] - lst[i][0] == distance:
            return [lst[i],lst[i+1]]

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def closest(string):
    if not string: return []
    # print(f"Start: {string}\n")
    n, out = [], []
    string = string.split()

    for i in range(len(string)):
        check = [sum_digits(int(string[i])), i, int(string[i])]
        n.append(check)
        # print(check)

    # print(f"N:{n}\n")
    weights = minDistance([list(tu) for tu in n])
    return weights

if __name__ == "__main__":
    print(closest(""), [])
    print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"), [[13, 9, 85], [14, 3, 176]])
    print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"), [[8, 5, 134], [8, 7, 62]])
    print(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"), [[10, 1, 154], [10, 9, 37]])
    print(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"), [[13, 3, 175], [14, 9, 167]])
    print(closest("462835 148 467467 128 183193 139 220167 116 263183 41 52"), [[13, 1, 148], [13, 5, 139]])
    print(closest("333188 132 20229 10 146007 123 39624 159 397062 180 161334 25 372766 46 39599 8 471523 88 379079 38 10160 10 368473 72 338658 21 386507 56 488250 39"), [[1, 3, 10], [1, 21, 10]])
