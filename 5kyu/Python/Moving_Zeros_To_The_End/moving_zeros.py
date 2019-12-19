#!/usr/bin/python3

def main(array):
	#print("Start array:", array)
	zeros = []
	non_zeros = []

	#array = [i for i in array if i != 0]
	for x in array:
		if isinstance(x, bool):
			non_zeros.append(x)
			continue

		if isinstance(x, list):
			for i in x:
				if isinstance(i, bool):
					continue
				if i == 0:
					zeros.append(i)
				else:
					pass

		if x == 0:
			zeros.append(x)
		else:
			non_zeros.append(x)

	#print("Non zeros:", non_zeros)
	#print("Zeros:", zeros)
	for i in zeros:
		non_zeros.append(round(i))

	#print(non_zeros)
	return non_zeros

if __name__ == '__main__':
	arr = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
	print(main(arr))
