import math
n = int(input())
for x in range(n):
  v,o,d,h1,h2 = map(float, input().split())
  t = d/(v*math.cos(o*math.pi/180))
  y = (v*t*math.sin(o*math.pi/180))-((.5)*(9.81)*(t**2))
  if(h1+1 <= y <= h2-1):
    print("Safe")
  else:
    print("Not Safe")