#!/usr/bin/env python3

# Count the smiley faces!
# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):
    count = 0
    valid = [':)', ':D', ';)', ';D', ':-)', ':~)',
            ':-D', ':~D', ';-)', ';~)', ';-D', ';~D']

    for i in arr:
        if i in valid:
            count += 1

    return count

if __name__ == '__main__':
    print(count_smileys([]), 0)
    print(count_smileys([':D',':~)',';~D',':)']), 4)
    print(count_smileys([':)',':(',':D',':O',':;']), 2)
    print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
