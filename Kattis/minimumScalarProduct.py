for i in range(int(input())):
  n,val = int(input()),0
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort(reverse = True)
  b.sort()
  
  for k in range(n):
    val += a[k]*b[k]
    
  print("Case #%d: %d" % (i+1,val))