x = 0
while True:
  x += 1
  n,k = int(input()), 0
  a,b,c = [], [], []
  
  if n == 0:
    break
  
  for i in range(n):
    a.append(input())
    
  for j in range(0,len(a)):
    if j % 2 == 0:
      b.append(a[j])
    else:
      c.append(a[j])
      
  print("SET %d" % x)
  print("\n".join(b))
  print("\n".join(c[::-1]))