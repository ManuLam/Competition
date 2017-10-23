import math
while True:
  try:
    a,b = map(int, input().split())
    print(int(math.fabs(a-b)))
  except EOFError:
    break