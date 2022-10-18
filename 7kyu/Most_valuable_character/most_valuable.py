#!/usr/bin/python3

def main(st):
   d = {}
   new = {}
   print(st)

   for index, letter in enumerate(st):
   	if not letter in d:
   		d[letter] = [index]
   	else:
   		d[letter].append(index)

   print(d)
   for key in d:
   	sub_value = abs(d[key][0] - d[key][-1])
   	print(key, sub_value)
   	new[key] = sub_value

   print(new)
   for k,v in sorted(new.items(),key=lambda x:(-x[1],x[0])):
       return "{} {}".format(k, v)

if __name__ == "__main__":
	st = 'aabccc'
	result = main(st)
	print(result)
