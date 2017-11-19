k,t = int(input()),0
c = ['N','P']

for i in range(int(input())):
  n,m = input().split()
  n = int(n)

  if m in c:
    t += n
    if(t >= 210):
      print(k)
      break
    
  elif m not in c:
    t += n
    if t >= 210:
      print(k)
      break;
    k += 1
 
  if(k == 9):
    k = 1