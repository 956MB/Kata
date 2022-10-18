#!/usr/bin/python3

# Rot13
# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(s):
    output, abc = "", "abcdefghijklmnopqrstuvwxyz"
    for l in s:
        if l.islower():
            output += abc[(abc.find(l) + 13) % 26]
        if l.isupper():
            output += abc.upper()[(abc.upper().find(l) + 13) % 26]
        if l in '0123456789!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ ':
            output += l
    return output


if __name__ == "__main__":
    print(rot13("test"), "grfg")
    print(rot13("Test"), "Grfg")
