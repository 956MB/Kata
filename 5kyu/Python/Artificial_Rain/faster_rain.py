#!/usr/bin/env python3

# Weight for weight
# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def artificial_rain(garden):
    if len(garden) == 1: return 1
    elif len(garden) == 0: return 0
    # print("Start: %s" % (garden))
    out = count = 1

    for i in range(0, len(garden)):
        r_last = l_last = start = i
        print("------------\nARR: %s, OUT: %d" % (garden, out))
        l, r = i-1, i+1
        if start == 0:
            l = 0
        elif i == len(garden)-1:
            r = len(garden)-1

        print("r_last: %d, l_last: %d, CURRENT: %d" % (r_last, l_last, garden[start]))
        print("L: %d, R: %d" % (garden[l], garden[r]))
        for x in range(0, len(garden)):
            if l == -1 and r == len(garden):
                print("EXCEPTION. l and r BOTH DONE")
                break
            # print("r_last %d | index: %d, l_last %d | index: %d" % (garden[r_last], r_last, garden[l_last], l_last))
            print("TETSING LOOP: %d" % (x))
            if start > 0:
                if l >= 0:
                    print("LEFT: %d, CURRENT: %d" % (garden[l], garden[l_last]))
                    if garden[l] <= garden[l_last]:
                        print("left: %d is less than %d, count += 1" % (garden[l], garden[l_last]))
                        count += 1
                        l_last = l
                        l -= 1
                    else:
                        l = -1

            if i < len(garden)-1:
                if r <= len(garden)-1:
                    print("CURRENT: %d, RIGHT: %d" % (garden[r_last], garden[r]))
                    if garden[r] <= garden[r_last]:
                        print("right: %d is <= %d, count += 1" % (garden[r], garden[r_last]))
                        count += 1
                        r_last = r
                        r += 1
                        print("UPDATED: r_last: %d, r: %d" % (r_last, r))
                    else:
                        # print("l num: %d" % (l))
                        if start <= 0:
                            break
                        else:
                            r = len(garden)

        if count > out:
            out = count

        count = 1

    return out

if __name__ == "__main__":
    print(artificial_rain([2]), 1)
    print(artificial_rain([1, 2, 1, 2, 1]), 3)
    print(artificial_rain([4, 2, 3, 3, 2]), 4)
    print(artificial_rain([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
