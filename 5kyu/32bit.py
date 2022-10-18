#!/usr/bin/env python3

# int32 to IPv4
# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python

def int32_to_ip(int32):
    return "{}.{}.{}.{}".format(((int32 >> 24) & 0xFF), ((int32 >> 16) & 0xFF), ((int32 >> 8 ) & 0XFF), (int32 & 0XFF))

if __name__ == '__main__':
    print(int32_to_ip(2154959208), int32_to_ip(2154959208) == "128.114.17.104") 
    print(int32_to_ip(0), int32_to_ip(0) == "0.0.0.0")
    print(int32_to_ip(2149583361), int32_to_ip(2149583361) == "128.32.10.1")