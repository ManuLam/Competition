import math
while True:
  a,b,c = map(float, input().split())
  if a == 0 and b == 0 and c == 0:
    break;
  print(math.pi*(a**2), 4*(a**2)*(c/b))