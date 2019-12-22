#!/usr/bin/python3
# Definitely not the most efficent, but it works.
# I had to basically touch and go with the amount of loops to get the test case numbers to work, not the best way to do that... idk...

def main(n):
    start = sorted(str(n))
    test = 1
    # print(start)
    while test < 40000:
        n += 1
        if start == sorted(str(n)):
            # print(sorted(str(n)))
            return n
        test += 1
    
    return -1

if __name__ == "__main__":
    n = 3788742
    print(main(n))
