import math
while True:
  x,y = map(int, input().split())
  if(x == 0 and y == 0):
    break;
  d1 = (x**3) - (6*y)/math.pi
  d = math.pow(d1, 1/3)
  print(d)