#!/usr/bin/python3

# Convert string to camel case
# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

import re, string, sys, base64

def run(input):
    return re.sub(r"[_-](\w)", lambda m: m.group(1).upper(), input)

if __name__ == "__main__":
    print(run(""), "")
    print(run("the_stealth_warrior"), "theStealthWarrior")
    print(run("The-Stealth-Warrior"), "TheStealthWarrior")
    print(run("A-B-C"), "ABC")