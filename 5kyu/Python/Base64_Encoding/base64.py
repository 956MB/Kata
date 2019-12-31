#!/usr/bin/python3
import base64
import re

def main(message):
   return re.sub(r'[^\w]', '', str(base64.b64encode(message.encode('utf-8')), 'utf-8'))

   # return str(base64.b64decode(message).decode('utf-8'))

if __name__ == "__main__":
   message = "J0XXvUeR55AHM"
   print(main(message))
