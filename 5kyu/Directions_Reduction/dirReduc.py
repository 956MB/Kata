#!/usr/bin/python3

def matching(last, current):
   if "NORTH" in last and current in "SOUTH":
      return True
   elif "SOUTH" in last and current in "NORTH":
      return True
   elif "WEST" in last and current in "EAST":
      return True
   elif "EAST" in last and current in "WEST":
      return True
   else:
      return False


def main(arr):
   print(arr)
   store = ""
   direc = []
   direcIndex = 0

   for i,v in enumerate(arr):
      print(direc, store, direcIndex)
      if v in store:
         direc.append(v)
         direcIndex += 1
         continue
      else:
         match = matching(store, v)
         print(match)
         if match:
            if len(direc) == 1:
               store = ""
               del direc[0]
               if direcIndex == 0:
                  continue
               else:
                  direcIndex -= 1
                  continue
            else:
               store = direc[direcIndex-1]
               del direc[direcIndex]
               if direcIndex == 0:
                  continue
               else:
                  direcIndex -= 1
                  continue
         else:
            direc.append(v)
            store = v

            if len(direc) <= 1:
               continue
            else:
               direcIndex += 1
               continue
   
   return direc

if __name__ == '__main__':
	a = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']
	# a = [north]
   # Return "West"
	print(main(a))
