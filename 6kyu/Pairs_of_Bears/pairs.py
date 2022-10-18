#!/usr/bin/python3

# Pairs of Bears
# https://www.codewars.com/kata/57d165ad95497ea150000020/train/python

def bears(x, s):
    pairs, count = '', 0
    it = zip(range(len(s)-1), s)

    for c,v in it:
        if v in 'B':
            if s[c+1] in '8':
                pairs += v + s[c+1]
                count += 1
                [next(it, None), 1]
        elif v in '8':
            if s[c+1] in 'B':
                pairs += v + s[c+1]
                count += 1
                [next(it, None), 1]

    return [pairs, count >= x]

if __name__ == '__main__':
    print(bears(7, '8j8mBliB8gimjB8B8jlB'), ["B8B8B8",False])
    print(bears(3, '88Bifk8hB8BB8BBBB888chl8BhBfd'), ["8BB8B8B88B",True])
    print(bears(8, '8'), ["",False])
    print(bears(1, 'j8BmB88B88gkBBlf8hg8888lbe88'), ["8BB88B",True])
    print(bears(0, '8j888aam'), ["",True])
