#!/usr/bin/python3

# Decoded String by the Numbers
# https://www.codewars.com/kata/562c3b54746f50d28d000027/train/python

def decode(string):
    out = []
    it = zip(range(len(string)), string)

    for c,v in it:
        # print(c,v)
        if v == '\\':
            num = int(string[c+1:c+3]) if string[c+2].isdigit() else int(string[c+1])
            lnum = len(str(num))
            section = string[c+lnum+1:c+num+lnum+1]
            out.append(section)
            [next(it, None) for _ in range(num+lnum)]
        else:
            out.append(v)

    return out

if __name__ == '__main__':
    print(decode(''), [])
    print(decode('abc'), ['a','b', 'c'])
    print(decode("\\1abc"), ['a', 'b', 'c'])
    print(decode("\\1a\\1bc"), ['a', 'b', 'c'])
    print(decode("\\3a\\1bc"), ['a\\1', 'b', 'c'])
    print(decode("\\10a\\1bc"), ['a\\1bc'])
    print(decode("\\10a\\1bc"), ['a\\1bc'])
    print(decode("abcd\\10efghijklmnop\\5qrstuvwx\\2yz"), ['a b c d efghijklmn o p qrstu w x yz'])
