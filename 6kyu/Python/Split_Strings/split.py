#!/usr/bin/python3


def split(s):
    if len(s) == 0:
        return []
    else:
        split = [s[i : i + 2] for i in range(0, len(s), 2)]
        if len(split[-1]) == 1:
            split[-1] += "_"
            return split
        return split


if __name__ == "__main__":
    s = "abcdef"
    print(split(s))
