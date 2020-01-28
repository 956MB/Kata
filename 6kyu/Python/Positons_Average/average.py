#!/usr/bin/python3

# Positions Average
# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python

def pos_average(s):
    total, matches = 0, 0
    nums = s.split(', ')
    print("\nStart:", nums)

    for l in range(0, len(nums)):
        for r in range(len(nums)-1, l, -1):
            # print(nums[l], nums[r])
            for m in range(0, len(nums[l])):
                if nums[l][m] == nums[r][m]:
                    # print(nums[l][m], nums[r][m])
                    matches += 1
                total += 1

            # print("---------------------")

    print(f"Total: {total}\nMatches: {matches}")
    percentage = 100 * float(matches)/float(total)

    return f"%: {round(percentage, 10)}\nAnswer:"
    # return round(percentage, 10)

if __name__ == '__main__':
    print(pos_average("6900690040, 4690606946, 9990494604"))
    print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"), 26.6666666667)
    print(pos_average("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"), 29.2592592593)
