#!/usr/bin/python3

def main(n):
    return f"({''.join(str(x) for x in n[0:3])}) {''.join(str(x) for x in n[3:6])}-{''.join(str(x) for x in n[6:10])}"

if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	print(main(arr))
