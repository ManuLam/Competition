import math
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
cir = (math.pi*60)

for i in range(int(input())):
  a = [x for x in input()]
  k =[min(abs(alpha.index(a[j-1]) - alpha.index(a[j])), 28 - abs(alpha.index(a[j-1]) - alpha.index(a[j]))) for j in range(1,len(a))]
  
  print(len(a) + (sum(k)*(cir/28))/15)