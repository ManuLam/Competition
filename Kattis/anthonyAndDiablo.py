import math
n,m = map(float, input().split())
r = m / (math.pi*2)
a = math.pi*(r**2)

if(n <= a):
  print("Diablo is happy!")
else:
  print("Need more materials!")