#!/usr/bin/env python3

import os
import argparse

def main():
    global kyu, name, link

    newkyu = os.path.realpath(kyu + "kyu")
    if not os.path.exists(newkyu): os.mkdir(newkyu)

    kata = os.path.join(newkyu, name)
    try:
        os.mkdir(kata)
    except OSError:
        exit("\"{}kyu/{}\" already exists".format(kyu, name))

    with open(os.path.join(kata, "{}.py".format(name)), "w") as f:
        f.write('''#!/usr/bin/python3

# {}
# {}

import re, string, sys, base64

def run(input):
    return input

if __name__ == "__main__":
    print(run(""))'''.format(name, link if link else "..."))

    print("({}, {}, {}) {}".format(kyu + "kyu", name, link, "Template created."))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Script for adding new Katas")
    opt = ap._action_groups.pop()
    opt.add_argument("-l","--link",type=str,nargs="?",help="link for new Kata")
    req = ap.add_argument_group("required arguments")
    req.add_argument("-k","--kyu",type=int,choices=range(1,9),nargs="?",help="level for new Kata (1kyu - 8kyu)")
    req.add_argument("-n","--name",type=str,help="name for new Kata")
    ap._action_groups.append(opt)
    args = vars(ap.parse_args())

    kyu, name, link = str(args["kyu"]), args["name"], args["link"]
    main()