#!/usr/bin/python3

def group_by_commas(s):
    split = [''.join(reversed(str(s)))[i : i + 3] for i in range(0, len(str(s)), 3)]
    return ''.join(reversed(','.join(split)))

if __name__ == "__main__":
    print(group_by_commas(1))
    print(group_by_commas(10))
    print(group_by_commas(100))
    print(group_by_commas(1000))
    print(group_by_commas(10000))
    print(group_by_commas(100000))
    print(group_by_commas(1000000))
    print(group_by_commas(35235235))
