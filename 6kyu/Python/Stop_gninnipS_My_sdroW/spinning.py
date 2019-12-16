#!/usr/bin/python3

def main(s):
	spin = ""

	for l in [a for b in s.split() for a in (b, ' ')][:-1]:
		if len(l) >= 5:
			for x in reversed(l):
				spin = spin + x
		else:
			spin = spin + l

	return spin

if __name__ == '__main__':
	s = "This is another test"
	result = main(s)
	print(result)
