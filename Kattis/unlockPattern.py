import math
s = [input().replace(" ","") for i in range(3)]
a,length = ''.join(s), 0
b = [(int(a.index(str(i))/3), s[int(a.index(str(i))/3)].index(str(i))) for i in range(1,10)]
x1,y1 = int(b[0][0]), int(b[0][1])

for x in b:
  if(x[0]-x1 == 0 or x[1]-y1 == 0): length += abs(x[0]-x1 + x[1]-y1)
  else: length += math.hypot(x[0]-x1,x[1]-y1)
  x1,y1 = x[0],x[1] 

print(length)