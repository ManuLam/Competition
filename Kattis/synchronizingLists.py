c = 0
while True:
  n = int(input())
  k,a,b = [],[],[]
  c += 1
  if(n == 0): break
  if(c > 1): print()
  
  for i in range(n):
    x = int(input())
    a.append(x)
    k.append(x)
    
  for i in range(n):
    b.append(int(input()))
    
  a.sort()
  b.sort()
  
  for i in range(n):
    print(b[a.index(k[i])])