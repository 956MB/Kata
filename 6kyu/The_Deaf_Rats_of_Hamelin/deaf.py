#!/usr/bin/python3

# The Deaf Rats of Hamelin
# https://www.codewars.com/kata/598106cb34e205e074000031/train/python
# you ever seen a more convoluted solution?

import re

def count_deaf_rats(town):
    new = town.replace(" ", "")
    ready = re.split(r'(P)', new)
    pPos = ready.index('P')
    left, right, count = "O~", "~O", 0

    for i in ready:
        if i in 'P':
            continue
        for n in range(0, len(i), 2):
            mouse = i[n:n+2]
            if ready.index(i) < pPos:
                if mouse in left:
                    count += 1
                    # print(mouse)
            elif ready.index(i) > pPos:
                if mouse in right:
                    count += 1
                    # print(mouse)

    return count

if __name__ == '__main__':
    print(count_deaf_rats("~O~O~O~O P"), 0)
    print(count_deaf_rats("P O~ O~ ~O O~"), 1)
    print(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)
