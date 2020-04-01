#!/usr/bin/env python3
# Break camelCase
# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

if __name__ == '__main__':
    print(solution("helloWorld"), "hello World")
    print(solution("camelCase"), "camel Case")
    print(solution("breakCamelCase"), "break Camel Case")
