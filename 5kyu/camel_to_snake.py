#!/usr/bin/env python3

# Convert PascalCase string into snake_case
# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

def to_underscore(string):
    if (isinstance(string, int)) or (string.isdecimal()): return str(string)
    temp, out, caps = string[0].lower(), [], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(1, len(string)):
        if string[i] in caps:
            out.append(temp)
            temp = ""
            temp += string[i].lower()
        else:
            temp += string[i]

    out.append(temp)
    return '_'.join(out)


if __name__ == '__main__':
    print(to_underscore('TestController') == 'test_controller', to_underscore('TestController'))
    print(to_underscore('MoviesAndBooks') == 'movies_and_books', to_underscore('MoviesAndBooks'))
    print(to_underscore('App7Test') == 'app7_test', to_underscore('App7Test'))