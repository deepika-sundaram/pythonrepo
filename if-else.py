If-else example:#!/bin/python3


import math
import os
import random
import re
import sys






if __name__ == '__main__':
    n = int(input().strip())
if(n%2==0):
    if(n>=6 and n<=20):
       print("Weird")
    else:
       print("Not Weird")
else:
  print("Weird")


Arithmetic operators-Example

:if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print (a-b)
    print (a*b)


for-Lopp example:
for i in range(0,n):
      print(i**2)


Function example:def is_leap(year):
    leap = False
   
    if(year%100==0):
      if(year%400==0):
         leap=True
    elif (year%4==0):
        leap=True
       
        # Write your logic here
   
    return leap


year = int(input())


 







