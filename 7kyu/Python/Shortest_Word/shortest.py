#!/usr/bin/python3

def main(s):
   split = sorted(s.split(' '), key = len)
   return len(split[0])

if __name__ == '__main__':
	s = "bitcoin take over the world maybe who knows perhaps"
	result = main(s)
	print(result)
