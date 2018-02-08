def tryIt():
  cap,n = map(int, input().split())
  x = 0
  for i in range(n):
    a,b,c = map(int, input().split())
    x -= a
    if((x) < 0):  return False
    x += b
    if(((x) > cap) or (cap > (x) and c != 0)): return False
    
  return x == 0
  
print("possible" if tryIt() else "impossible")