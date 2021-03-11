#!/usr/bin/python3

# How many numbers III?
# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

# def find_all(sum_dig, digs):
    # match, matches = True, 0
    # s, l = int("9"*digs), 0

    # for num in range(int("9"*(digs-1))+1, int("9"*digs)+1):
        # if sum_digits(num) == sum_dig:
            # for n in range(0, len(str(num))-1):
                # _0 = int(str(num)[n])
                # _next = int(str(num)[n+1])
                # if _next >= _0:
                    # pass
                # else:
                    # match = False
                    # break

            # if match:
                # matches += 1
                # if num < s:
                    # s = num
                # elif num > l:
                    # l = num
            # else:
                # match = True

        # else:
            # pass

    # if matches == 0: return []
    # return [matches, s, l]


def sum_digits(n):
    _sum = 0
    while n:
        _sum, n = _sum + n % 10, n // 10
    return _sum


def find_all(sum_dig, digs):
    matches, count, last = [], 0, 0
    print("start sum: %d, digits: %d" % (sum_dig, digs))

    for num in range(int("9"*(digs-1))+1, int("9"*digs)+1):
        if sum_digits(num) == sum_dig:
            if num == int(''.join(sorted(str(num)))):
                print("diff from last: %d" % (num-last))
                last = num
                print("num: %d, count: %d\n" % (num, count))
                count += 1
                matches.append(num)
            # for n in range(0, len(str(num))-1):
                # if int(str(num)[n+1]) >= int(str(num)[n]):
                    # pass
                # else:
                    # match = False
                    # break

            # if match:
                # matches.append(num)
            # else:
                # match = True

    if len(matches) == 0: return matches
    return [len(matches), min(matches), max(matches)]
    # return matches


if __name__ == '__main__':
    # print(find_all(10, 3), [8, 118, 334])
    # print(find_all(27, 3), [1, 999, 999])
    # print(find_all(84, 4), [])
    print(find_all(35, 6), [123, 116999, 566666])
    # print(find_all(65, 7), ['??'])
    # print(find_all(105, 17), ['??'])
