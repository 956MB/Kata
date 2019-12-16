#!/usr/bin/python3

def main(n):
	if n < 10:
		return 0
	else:
		digits = 0
		for x in range(len(str(n)) + 1):
			if len(str(n)) == 1:
				return digits
			n = multi(list(map(int,str(n))))
			# print(n)
			digits += 1

	return digits

def multi(li):
	r = 1
	for x in li:
	  r = r * x

	return r

if __name__ == '__main__':
	n = 999
	result = main(n)
	print(result)
