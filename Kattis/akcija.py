n,k,c = int(input()),0,-1
a = []

for i in range(n):
  a.append(int(input()))

a.sort(reverse = True)
if(n < 3): print(sum(a))
  
else:
  while((n-1) - c >= 3):
    c += 3
    a[c] = 0
  print(sum(a))