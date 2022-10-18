#!/usr/bin/python3
import re

def score_hand(cards):
   hand = 0
   aces = 0
   for i in cards:
      if i in 'JQK':
         hand += 10
      elif i in 'A':
         aces += 1
         hand += 11
      else:
         hand += int(i)
   
   if hand >= 22:
      hand -= 10 * aces
      if hand + 10 <= 21:
         hand += 10
   return hand

if __name__ == "__main__":
   # arr = ['A', '2', 'A', '9', '9']
   # print(main(arr))
   print(score_hand(['2', '3']))
   print(score_hand(['7', '7', '8']))
   print(score_hand(['4', '7', '8']))
   print(score_hand(['K', 'J','Q']))
   print(score_hand(['A', '3']))
   print(score_hand(['A', 'A']))
   print(score_hand(['A', '2', 'A', '9', '9']))