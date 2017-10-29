import math
n,w,h = map(int, input().split())
limit = int(math.sqrt((w**2)+(h**2)))

for i in range(n):
  print("DA") if(limit >= int(input())) else print("NE")