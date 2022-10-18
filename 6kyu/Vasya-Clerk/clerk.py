#!/usr/bin/python3
# 25, 25, 50, 50, 100
# 50, 50 : NO


# 25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100
# 25, 100, 100, 100 : 325

def main(people):
	print(people)
	ticket = 25
	bills = []
	# change = bill they give me - 25

	for x in people:
		change = x - 25
		if change == 0: # No change to be given
			bills.append(x)
		elif change == 25:
			if change in bills:
				bills.remove(change)
				bills.append(x)
			else:
				return "NO"
		elif change == 75:
			if sum(bills) >= 75:
				if all(i in bills for i in [25, 50]):
					print(bills)
					for x in [25, 50]:
						bills.remove(x)
					bills.append(100)
				elif bills.count(25) == 3:
					for x in [25, 25, 25]:
						bills.remove(x)
					bills.append(100)
				else:
					return "NO"
			else:
				return "NO"
		print(bills)

	print(bills)
	return "YES"

if __name__ == '__main__':
	people = [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]
	result = main(people)
	print(result)
