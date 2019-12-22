#!/usr/bin/python3

def main(arr):
    d = {}
    for n in arr:
        if not n in d:
            d[n] = 1
        else:
            d[n] += 1
    
    for k,v in d.items():
        if not v % 2 == 0:
            return k

if __name__ == '__main__':
	arr = [10]
	print(main(arr))
