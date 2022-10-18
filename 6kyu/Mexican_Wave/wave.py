#!/usr/bin/python3

def main(string):
   arr = []
   test = string.lower()

   for i in range(0, len(test)):
      if test[i] in ' ':
         continue
      arr.append("{}{}{}".format(test[:i], test[i].capitalize(), test[i+1:]))

   return arr

if __name__ == "__main__":
   diamond = " Gap "
   print(main(diamond))
