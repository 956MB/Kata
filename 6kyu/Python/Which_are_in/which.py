#!/usr/bin/python3

# Which are in?
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(a1, a2):
    d = {}
    for _1 in a1:
        for _2 in a2:
            if _1 in _2:
                if not _1 in d:
                    d[_1] = 1
                else:
                    d[_1] += 1

    return sorted(d)

if __name__ == '__main__':
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(in_array(a1, a2), ['arp', 'live', 'strong'])
