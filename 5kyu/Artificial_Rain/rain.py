#!/usr/bin/env python3

# Weight for weight
# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def artificial_rain(garden):
    if len(garden) == 1: return 1
    elif len(garden) == 0: return 0
    # print("Start: %s" % (garden))
    start, count, check = 1, 1, True

    for i in range(0, len(garden)):
        # print("-----------\nstart number: %d" % (start))
        # print("arr: %s" % (garden))
        # print("Current: %d, Index: %d" % (garden[i], i))
        last = rev_last = garden[i]
        # print("restart last: %d" % (last))
        for x in range(i+1, len(garden)):
            # print("Next forward: %d" % (garden[x]))
            # print("last %d" % (last))
            if garden[x] <= last:
                # print("Next smaller, Increase count")
                count += 1
                last = garden[x]
            else:
                # print("Next larger, skip")
                last = garden[x]
                break
            for y in range(i, 0, -1):
                if check:
                    # print("Next back: %d" % (garden[y-1]))
                    if garden[y-1] <= rev_last:
                        # print("Reversse smaller, Increase count")
                        count += 1
                        rev_last = garden[y-1]
                    else:
                        # print("Reverse larger, skip")
                        check = False

        if count > start:
            start = count

        count, check = 1, True

    return start

if __name__ == "__main__":
    print(artificial_rain([2]), 1)
    print(artificial_rain([1, 2, 1, 2, 1]), 3)
    print(artificial_rain([4, 2, 3, 3, 2]), 4)
