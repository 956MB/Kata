#!/usr/bin/python3

# What will be the odd one out?
# https://www.codewars.com/kata/55b080eabb080cd6f8000035/train/python

def odd_one_out(s):
    # print("Start:", s)
    d, out = {}, []
    for i in s:
        if not i in d:
            d[i] = 1
        else:
            val = d[i]
            del d[i]
            d[i] = val + 1

    for k,v in d.items():
        if (v % 2) != 0:
            out.append(k)

    # print(d)
    return out

if __name__ == '__main__':
    print(odd_one_out('Hello World'), ["H", "e", " ", "W", "r", "l", "d"])
    print(odd_one_out('Codewars'), ["C", "o", "d", "e", "w", "a", "r", "s"])
    print(odd_one_out('woowee'), [])
    print(odd_one_out('wwoooowweeee'), [])
    print(odd_one_out('racecar'), ["e"])
    print(odd_one_out('Mamma'), ["M"])
    print(odd_one_out('Mama'), ["M", "m"])
    print(odd_one_out('¼ x 4 = 1'), ["¼", "x", "4", "=", "1"])
    print(odd_one_out('¼ x 4 = 1 and ½ x 4 = 2'), ["¼", "1", "a", "n", "d", "½", "2"])
