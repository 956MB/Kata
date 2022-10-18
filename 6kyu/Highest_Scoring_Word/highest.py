#!/usr/bin/python3
import re
import string

def high(x):
   d = {}
   temp = 0

   for w in x.split():
      for l in w:
         temp += string.ascii_lowercase.index(l) + 1

      if not w in d:
         d[w] = temp
      else:
         d[w] += temp
      
      temp = 0

   # print(d)
   return sorted(d, key=d.get, reverse=True)[0]
   # print(string.ascii_lowercase.index(test))

if __name__ == "__main__":
   # arr = ['A', '2', 'A', '9', '9']
   # print(main(arr))
   print(high('man i need a taxi up to ubud'))
   print(high('what time are we climbing up the volcano'))
   print(high('take me to semynak'))