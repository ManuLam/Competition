def func(i):
  if(i % 2 != 0): return False
  visited = [0,0,0,0,0,0,0,0,0,0]
  temp = i
  while(i):
    x = i%10
    if (visited[x] == 1) or (x == 0): break
    visited[x] = 1; 
    i = (int)(i / 10); 

  if(i == 0):
    for y in str(temp):
      if(temp % int(y) != 0): return False

  else: return False
  return True

n,m = map(int, input().split())

print(sum([1 for i in range(n,m) if func(i)]))