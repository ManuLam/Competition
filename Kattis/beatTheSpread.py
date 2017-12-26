n = int(input())
for i in range(n):
  p,q = map(int, input().split())
  k = p + q
  
  if(p < q):  print("impossible")
  elif(k/2 != int(k/2)): print("impossible")
  else: print(int(k/2), int(k/2)-q)