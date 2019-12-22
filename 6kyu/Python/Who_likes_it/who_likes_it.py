#!/usr/bin/python3

def main(names):
	if len(names) == 0: return f"no one likes this"
	if len(names) == 1: return f"{names[0]} likes this"
	if len(names) == 2: return f"{names[0]} and {names[1]} like this"
	if len(names) == 3: return f"{names[0]}, {names[1]} and {names[2]} like this"
	if len(names) >= 4: return f"{names[0]}, {names[1]} and {len(names)-2} others like this"

if __name__ == '__main__':
	names = ['Max', 'John', 'Mark']
	print(main(names))
