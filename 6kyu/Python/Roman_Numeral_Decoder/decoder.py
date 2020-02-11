#!/usr/bin/python3

# Roman Numerals Decoder
# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(roman):
    print(f"Start: {roman}")
    arr = convert(roman)
    total, last = 0, arr[0]
    print(f"Change: {arr}")

    for i in arr:
        current = i
        if i > last:
            total -= last
            total += abs(last - current)
        else:
            total += current
            last = current

    return total

def convert(roman):
    convert = []

    for i in roman:
        if i == 'I':
            convert.append(1)
        elif i == 'V':
            convert.append(5)
        elif i == 'X':
            convert.append(10)
        elif i == 'L':
            convert.append(50)
        elif i == 'C':
            convert.append(100)
        elif i == 'D':
            convert.append(500)
        elif i == 'M':
            convert.append(1000)

    return convert

if __name__ == '__main__':
    print(solution('XXI'), 21, 'XXI should == 21\n')
    print(solution('I'), 1, 'I should == 1\n')
    print(solution('IV'), 4, 'IV should == 4\n')
    print(solution('MMVIII'), 2008, 'MMVIII should == 2008\n')
    print(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666\n')
    print(solution('MCMXC'), 1990, 'MCMXC should == 1990\n')
