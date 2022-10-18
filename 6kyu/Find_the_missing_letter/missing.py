#!/usr/bin/python3

def main(chars):
	alpha = 'abcdefghijklmnopqrstuvwxyz' if chars[0] >= 'a' else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in alpha[alpha.index(chars[0]):]:
		if letter not in chars:
			return letter[0]

if __name__ == '__main__':
	chars = ['O','Q','R','S']
	result = main(chars)
	print(result)
