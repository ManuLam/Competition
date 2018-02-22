a,b = [0, 1], [1, 0]

for i in range(2,31):
  b.append(a[i-1]*2 + b[i-2])
  a.append(a[i-2] + b[i-1])
  
while True:
  x = int(input())
  if(x == -1): break
  print(b[x])