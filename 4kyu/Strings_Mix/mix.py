#!/usr/bin/python3

# Strings Mix
# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python

from itertools import chain

def mix(s1, s2):
    # print(f'Start s1: {s1} | Start s2: {s2}')
    s1, s2 = ''.join(c for c in s1 if c.islower()), ''.join(c for c in s2 if c.islower())
    out, d1, d2, final = '/', {}, {}, {}
    # print(f'Compressed s1: {s1} | Compressed s2: {s2}')

    for _1 in s1:
        if not _1 in d1:
            d1[_1] = 1
        else:
            d1[_1] += 1

    for _2 in s2:
        if not _2 in d2:
            d2[_2] = 1
        else:
            d2[_2] += 1

    for k,v in chain(d1.items(), d2.items()):
        if v > 1:
            try:
                if d1[k] > d2[k]:
                    final[f'1:{k}'] = d1[k]
                elif d1[k] < d2[k]:
                    final[f'2:{k}'] = d2[k]
                elif d1[k] == d2[k]:
                    final[f'=:{k}'] = v
            except KeyError:
                if k in d1.keys():
                    final[f'1:{k}'] = v
                    # print(f'{k} in d1')
                elif k in d2.keys():
                    final[f'2:{k}'] = v
                    # print(f'{k} in d2')

    final = sorted(final.items(), key=lambda x:(-x[1], x[0]))
    # print(f'D1: {d1}\nD2: {d2}')
    # print(f'Final: {final}')

    for k in final:
        begin = k[0][0:2]
        letter = k[0][-1]
        num = k[1]
        out += f'{begin}{letter*num}/'

    return out[1:-1]

if __name__ == "__main__":
    print(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
    print(mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    print(mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    print(mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo")
    print(mix("codewars", "codewars") == "")
    print(mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
