#!/usr/bin/python3

def main(iterable):
	print(iterable)
	store = ''
	new = []
	for x in iterable:
		print(store, new)
		if x == store:
			pass
		else:
			store = x
			new.append(x)

	return new

if __name__ == '__main__':
	s = [1,2,2,3,3]
	result = main(s)
	print(result)
