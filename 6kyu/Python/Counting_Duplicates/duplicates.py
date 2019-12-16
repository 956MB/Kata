#!/usr/bin/python3

def main(s):
	d = {}
	add = 0

	for l in s.lower():
		if not l in d:
			d[l] = 1
		else:
			d[l] += 1

	for i in d:
		if d[i] >= 2:
			add += 1

	print(d)
	return add

if __name__ == '__main__':
	s = "indivisibility"
	result = main(s)
	print(result)
