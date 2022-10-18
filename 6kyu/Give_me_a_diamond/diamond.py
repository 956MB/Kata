#!/usr/bin/python3

def main(n):
   if (n % 2) == 0:
      return None
   elif n <= 0:
      return None

   temp = 0
   l = n
   while l > 1:
      l -= 2
      temp += 1
   
   store = temp
   start = 1
   diamond = ""
   
   for i in range(1, n-temp+1):
      diamond += f"{' '*temp}{'*'*start}\n"
      start += 2
      if temp == 0:
         continue
      temp -= 1

   start = n
   temp += 1
   for x in range(1, store+1):
      diamond += f"{' '*temp}{'*'*(start-2)}\n"
      start -= 2
      temp += 1
   
   return diamond
   # print(repr(string))


if __name__ == "__main__":
   diamond = 7
   print(main(diamond))
