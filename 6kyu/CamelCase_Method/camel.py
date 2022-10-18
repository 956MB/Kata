#!/usr/bin/python3

def main(string):
    if len(string) == 0: 
        return string
    return ''.join(i.capitalize() for i in string.lower().split())

if __name__ == "__main__":
    print(camel_case("test case"))
    print(camel_case("camel case method"))
    print(camel_case("say hello "))
    print(camel_case(" camel case word"))
    print(camel_case(""))