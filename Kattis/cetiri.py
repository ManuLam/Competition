aR = sorted([int(x) for x in input().split()])
a,b,c = aR[0], aR[1], aR[2]
d1,d2 = b-a, c-b

if(d1 == d2):
  print(c+d1)
  
elif(d1 > d2):
  print(a+d2)
  
else:
  print(b+d1)