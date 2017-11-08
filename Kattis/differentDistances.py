import math
while True:
  try:
    x1,y1,x2,y2,p = map(float, input().split())
    print(((math.fabs(x1-x2)**p) + (math.fabs(y1-y2)**p))**(1/p))
  except ValueError:
    break