#!/usr/bin/env python3

# Tongues
# https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8/train/python

def tongues(code):
    vL, vU, cL, cU, out = 'aiyeou', 'AIYEOU', 'bkxznhdcwgpvjqtsrlmf', 'BKXZNHDCWGPVJQTSRLMF', ''

    for i in range(0, len(code)):
        if code[i] in vL: out += vL[(vL.index(code[i]) + 3) % 6]
        elif code[i] in vU: out += vU[(vU.index(code[i]) + 3) % 6]
        elif code[i] in cL: out += cL[(cL.index(code[i]) + 10) % 20]
        elif code[i] in cU: out += cU[(cU.index(code[i]) + 10) % 20]
        else: out += code[i]

    return out

if __name__ == '__main__':
    print(tongues('Ita dotf ni dyca nsaw ecc.') == 'One ring to rule them all.')
    print(tongues('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.') == 'Now is the time for all good men to come to the aid of their country.')
    print(tongues('Giydhlida etr hakat uaedh efi iyd gidagensadh pdiyfsn ytni nsoh') == 'Fourscore and seven years ago our forefathers brought unto this')
    print(tongues('litnotatn e tam tenoit.') == 'continent a new nation.')
    print(tongues('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.') == 'The quick brown fox jumped over the lazy dogs.')