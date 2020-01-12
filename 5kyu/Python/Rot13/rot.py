#!/usr/bin/python3

import string

def rot13(s):
    output = ""
    for l in s:
        if l.islower():
            output += string.ascii_lowercase[(string.ascii_lowercase.find(l) + 13) % 26]
        if l.isupper():
            output += string.ascii_uppercase[(string.ascii_uppercase.find(l) + 13) % 26]
        if l in '0123456789!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ ':
            output += l
    return output


if __name__ == "__main__":
    print(rot13("test"))
    print(rot13("Test"))