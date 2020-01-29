#!/usr/bin/python3

# String -> N iterations -> String
# https://www.codewars.com/kata/5ae43ed6252e666a6b0000a4/train/python

def jumbled_string_mod(s, n):
    # "jumble" until it gets back to its orignal string.
    # last iteration is the number to mod 'n' by
    og = s
    print(f'Start: {s}, n: {n}')
    for i in range(1, n+1):
        s = ''.join(list(s)[::2] + list(s)[1::2])
        if s == og:
            return f'\nBack to OG: {s}, {i} iterations.\n'
        print(f'{i} Change: {s}')

    return f'Final: {s}, {i} iterations.\n'

def jumbled_string(s, n):
    m = 0
    og = s
    # first "jumble" loop to get string back to original.
    for i in range(1, n+1):
        s = ''.join(list(s)[::2] + list(s)[1::2])
        if s == og:
            m = i
            break

    # then if 'm'(iteration number) is greater than 0 (it returned to original string)
    # use 'm' to mod original 'n' (n % m). loop that many times, return jumbled string.
    if m == 0: return s
    s = og
    n = n % m
    for _ in range(n):
        s = ''.join(list(s)[::2] + list(s)[1::2])

    return s

if __name__ == "__main__":
    print("Sc o!uhWw",jumbled_string("Such Wow!",1))
    print("bexltept merae",jumbled_string("better example",2))
    print("qtorieuwy",jumbled_string("qwertyuio",2))
    print("qtorieuwy", jumbled_string("qwertyuio",8764390076))
    print("Gtsegenri",jumbled_string("Greetings",8))
    print("criyinodedsgufrnodnoser", jumbled_string("codingisfornerdsyounerd",10101010))
