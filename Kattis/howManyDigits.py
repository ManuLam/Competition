import math
k = [0] * 1000001

for i in range(1, 1000001):
  k[i] += k[i-1] + math.log10(i)
      
while True:
  try:
    print(int(k[int(input())]) + 1)
    
  except EOFError:
    break