#!/usr/bin/python3

def main(r, g, b):
	rgb = [r, g, b]
	print(rgb)
	for x, v in enumerate(rgb):
		if v > 255:
			rgb[x] = 255
		elif v < 0:
			rgb[x] = 0
	print(rgb)
	return '%02x%02x%02x'.upper() % tuple(rgb)

if __name__ == '__main__':
	r = -20
	g = 275
	b = 125
	result = main(r, g, b)
	print(result)
