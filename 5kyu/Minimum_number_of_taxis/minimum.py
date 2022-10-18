#!/usr/bin/python3

def min_num_taxis(arr):
    active = []
    pickup, drop, count = 0, 0, 0

if __name__ == "__main__":
    one_req = [(1,4)] # One request, one taxi.
    print(min_num_taxis(one_req), 1)
    two_reqs = [(1,4), (5, 9)] # Two requests, one taxi.
    print(min_num_taxis(two_reqs), 1)
    three_reqs = [(1,4), (2, 9), (3, 6)] # Three requests, three taxis.
    print(min_num_taxis(three_reqs), 3)
    four_reqs = [(1,4), (2, 9), (3, 6), (5, 8)] # Four requests, three taxis.
    print(min_num_taxis(four_reqs), 3)
