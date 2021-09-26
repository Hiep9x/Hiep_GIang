# t = int(input())

# for i in range(0,t):
#  n,x = list(map(int,input().split()))
#  if n == 1:
#      print("1")
#  elif n == 2:
#      print("1")
#  elif x == 1:
#      print(round(n/x)-1)
#  elif n/x == 1.5:
#     print("2")
#  elif n < x  :   
#         print("2")
#  elif n%x == 0:
#     print(int(n/x))
#  else:
#      print(round(n/x)+1)

import math

t = int(input())

for i in range(0,t):
 n,x = list(map(int,input().split()))
 if n == 1:
     print("1")
 elif n == 2:
     print("1")
 elif n <= x:
     print("2")
 elif n>x: 
     if n/x <= 2:
         print("2")
     elif n/x >2:
         if x == 1:
          print(round(n/x)-1)
         if x != 1: 
          print(round(n/x) + 1)

