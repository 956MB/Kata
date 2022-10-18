#!/usr/bin/env python3

# Convert A Hex String To RGB
# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python

def hex_string_to_RGB(hex_string):
    return {'r':int(hex_string[1:3], 16), 'g':int(hex_string[3:5], 16), 'b':int(hex_string[5:7], 16)}

if __name__ == '__main__':
    print(hex_string_to_RGB("#FF9933") == {'r':255, 'g':153, 'b':51})
    print(hex_string_to_RGB("#beaded") == {'r':190, 'g':173, 'b':237})
    print(hex_string_to_RGB("#000000") == {'r':0, 'g':0, 'b':0})
    print(hex_string_to_RGB("#111111") == {'r':17, 'g':17, 'b':17})
    print(hex_string_to_RGB("#Fa3456") == {'r':250, 'g':52, 'b':86})