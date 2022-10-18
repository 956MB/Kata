#!/usr/bin/python3

# Packing your backpack
# https://www.codewars.com/kata/5a51717fa7ca4d133f001fdf/train/python

def pick_peaks(arr):
    print("\nstart {}".format(arr))
    # pos, peaks = [], []
    d = {"pos":[], "peaks":[]}

    for i,v in enumerate(arr[1:-1], 1):
        if arr[i-1] < v > arr[i+1]:
            # print(f"peak: {arr[i-1]},{v},{arr[i+1]}")
            d["pos"].append(i)
            d["peaks"].append(v)
        elif arr[i-1] == v == arr[i+1]:
            # print(f"equal: {arr[i-1]},{v},{arr[i+1]}")
            d["pos"].append(i-1)
            d["peaks"].append(v)

    return d
            # return "YEP {},{}".format(arr[i-1], arr[i+1])
        # print(i,v)

if __name__ == "__main__":
    # print(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
    # print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
    # print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
    print(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
    print(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
    print(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
    print(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
    print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
    # print(pick_peaks([]),{"pos":[],"peaks":[]})
    # print(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})
