#!/usr/bin/python3

def main(string):
   out = ""

   for x in [y for z in string.split() for y in (z, ' ')][:-1]:
      if x in ' ':
         out += x
         continue
      for l in range(len(x)):
         if (l % 2) == 0:
            out += x[l].upper()
         else:
            out += x[l].lower()
         
   return out

if __name__ == "__main__":
   string = "This is a test"
   print(main(string))
