#!/usr/bin/python3

def calculate(s):
    return str(eval(s.replace('plus', '+').replace('minus', '-')))

if __name__ == "__main__":
    print(calculate('1plus2plus3plus4'))
    print(calculate('1minus2minus3minus4'))
    print(calculate('1plus2plus3minus4'))