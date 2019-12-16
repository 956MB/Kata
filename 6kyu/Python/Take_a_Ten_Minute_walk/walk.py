#!/usr/bin/python3

def main(walk):
	#print(walk)
	if len(walk) == 10:
		start = [0, 0]
		new = [0, 0]
		#print("STart:", start)
		for d in walk:
			if 'n' in d:
				new[1] -= 1
			elif 's' in d:
				new[1] += 1
			elif 'e' in d:
				new[0] += 1
			elif 'w' in d:
				new[0] -= 1
			#print(new)
		if new == start:
			return True
		else:
			return False
	else:
		return False

if __name__ == '__main__':
	result = main(['e', 'n', 's', 's', 'w', 'n', 's', 'n', 'e', 'w'])
	print(result)