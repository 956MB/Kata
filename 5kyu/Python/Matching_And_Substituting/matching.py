#!/usr/bin/env python3

# Matching And Substituting
# https://www.codewars.com/kata/59de1e2fe50813a046000124/train/python

import re

def change(s, prog, version):
    s = s.split('\n')
    vers = s[5].split()[1]
    phone = s[3].split()[1]

    if re.match(r"^(\d){1,}\.(\d){1,}$", vers):
        if vers in "2.0":
            vers = vers
        else:
            vers = version
    else:
        return "ERROR: VERSION or PHONE"

    if re.match(r"^\+1-(\d){3}-(\d){3}-(\d){4}$", phone):
        phone = "+1-503-555-0090"
    else:
        return "ERROR: VERSION or PHONE"

    return f"Program: {prog} Author: g964 Phone: {phone} Date: 2019-01-01 Version: {vers}"

if __name__ == "__main__":
    s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
    s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
    s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-009\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'

    print(change(s1, 'Ladder', '1.1'), 'Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1')
    print(change(s11, 'Balance', '1.5.6'), 'Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0')
    print(change(s12, 'Ladder', '1.1'), 'ERROR: VERSION or PHONE')
