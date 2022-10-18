#!/usr/bin/python3

# Most frequently used words in a text
# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

import re

# regex along the way:
# [,\.!?:;><!@#$%^&*\(\{\[\]\}\)-_=+|/~`]
# ([,\\.!?:;><!@#$%^&*\(\{\[\]\}\)_=+|/~`]|[-'\ ]+[-'][-'\ ]+)

def top_3_words(text):
    # print("Text:", repr(text))
    d = {}
    regex = re.compile("([-,\\.!?:;><!@#$%^&*\(\{\[\]\}\)_=+|/~`]|[-'\ ]+[-'][-'\ ]+)")
    text = regex.sub(' ', text.lower())
    # print("After", repr(text), "\n")

    for w in text.lower().split():
        if not w in d:
            d[w] = 1
        else:
            d[w] += 1

    # print(d)
    results = sorted(d, key=d.get, reverse=True)[:3]

    if len(results) > 3:
        return results[:3]
    else:
        return results

if __name__ == "__main__":
    print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    print(top_3_words("  //wont won't won't "), ["won't", "wont"])
    print(top_3_words("  , e   .. "), ["e"])
    print(top_3_words("  ...  "), [])
    print(top_3_words("  '  "), [])
    print(top_3_words("  '''  "), [])
    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
