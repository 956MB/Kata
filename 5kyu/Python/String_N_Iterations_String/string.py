#!/usr/bin/python3

def main(string, n):
   even = ""
   odd = ""

   for i in range(n):
      # string = ''.join(list(string)[::2] + list(string)[1::2])
      for c in range(len(string)):
         if (c % 2) == 0:
            even += string[c]
         else:
            odd += string[c]

      string = even + odd
      even = ""
      odd = ""

   return string

if __name__ == "__main__":
   n = 2
   string = "better example"
   print(main(string, n))
