#!/usr/bin/python3
import re

def main(string):
   match = re.search(r'[a-zA-Z@_!#$%^&*()<>?/\|}\-{~:]', string)
   if match:
      return False

   if len(string) == 0:
      return False
   elif (len(string) % 2) == 0:
      left = string[:len(string)//2]
      right = string[len(string)//2:]
   else:
      left = string[:len(string)//2]
      right = string[len(string)//2 + 1:]
      
   left_sum = sum(int(x) for x in left if x.isdigit())
   right_sum = sum(int(x) for x in right if x.isdigit())

   # print(left_sum, right_sum)
   return left_sum == right_sum

if __name__ == "__main__":
   num = "6F43E8"
   print(main(num))