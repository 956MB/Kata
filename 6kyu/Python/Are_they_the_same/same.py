#!/usr/bin/python3

# Are they the "same"?
# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1 and array2:
        return sorted([i**2 for i in array1]) == sorted(array2)
    else:
        return array1 == array2 == []

if __name__ == '__main__':
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]), True)
    print(comp([], [121, 14641, 20736, 361, 25921, 361, 20736, 361]), False)
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]), True)
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]), False)
    print(comp([], []), True)
    print(comp([], None), False)
