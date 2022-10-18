#!/usr/bin/env python3

# ISBN-10 Validation
# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001

# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

def valid_ISBN10(isbn):
    if (isbn.count('X') > 1) or (not (10 <= len(isbn) <= 10)): return False
    out, let = 0, 'ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz'

    for i in range(0, 10):
        v = isbn[i]
        if (v in let) or ((i != 9) and (v == 'X')): return False
        v = 10 if v == 'X' else int(v)
        out += v*(i+1)

    return (out % 11) == 0

if __name__ == '__main__':
    print(valid_ISBN10('1112223339') == True)
    print(valid_ISBN10('048665088X') == True)
    print(valid_ISBN10('1293000000') == True)
    print(valid_ISBN10('1234554321') == True)
    print(valid_ISBN10('1234512345') == False)
    print(valid_ISBN10('1293') == False) #g
    print(valid_ISBN10('X123456788') == False)
    print(valid_ISBN10('ABCDEFGHIJ') == False)
    print(valid_ISBN10('XXXXXXXXXX') == False)#g