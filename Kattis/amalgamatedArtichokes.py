import math
p,a,b,c,d,n = map(int, input().split())
k = [(p * (math.sin(a*i + b) + math.cos(c*i + d) + 2)) for i in range(1, n+1)]

x,y = 0, 0
def check(q):
  global x,y 
  x,y = max(x, y-q), max(y, q)
  return x
  
print(max([check(q) for q in k]))