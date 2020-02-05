#!/usr/bin/python3

# How Many Numbers? II
# https://www.codewars.com/kata/55f5efd21ad2b48895000040/train/python

def max_sumDig(nMax, maxSum):
    match, matches = True, []

    for num in range(1000, nMax+1):
        for n in range(0, len(str(num))-4+1):
            _1 = list(map(int, str(num)[n:n+4]))
            if 0 <= sum(_1) <= maxSum:
                pass
            else:
                match = False
                break

        if match:
            # print(f'Num: {num}, Sum: {sum(_1)}')
            matches.append(num)
        else:
            match = True

    mean = sum(matches)/len(matches)
    return [len(matches), min(matches, key=lambda x:abs(x-mean)), sum(matches)]

if __name__ == '__main__':
    print(max_sumDig(2000, 3), [11, 1110, 12555])
    print(max_sumDig(2000, 4), [21, 1120, 23665])
    print(max_sumDig(2000, 7), [85, 1200, 99986])
    print(max_sumDig(3000, 7), [141, 1600, 220756])
    print(max_sumDig(4000, 4), [35, 2000, 58331])
    print(max_sumDig(5000, 6), [122, 2010, 244875])
    print(max_sumDig(87145, 8), [1914, 24202, 46458126])
