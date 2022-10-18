#!/usr/bin/python3

def main(integers):
    o = 0
    e = 0
    for n in integers:
        if e == 2:
            break
        elif o == 2:
            break

        if n % 2 == 0:
            e += 1
        else:
            o += 1

    if o > e:
        for i in integers:
            if i % 2 == 0: return i
    else:
        for i in integers:
            if not i % 2 == 0: return i

if __name__ == '__main__':
	arr = [160, 3, 1719, 19, 11, 13, -21]
	print(main(arr))
