#!/usr/bin/python3
 
def main(n):
    i = 5
    result = 0

    while n >= i:
        result += n // i
        i *= 5

    return result

if __name__ == "__main__":
    n = 30
    print(main(n))