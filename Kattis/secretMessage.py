import math
for i in range(int(input())):
  s = input()
  a = [str(p) for p in s]
  b = []
  
  if(math.sqrt(len(a)) == int(math.sqrt(len(a)))):
    x = int(math.sqrt(len(a)))
  else:
    x = int(math.sqrt(len(a))) + 1
    for i in range((x*x)-len(a)):
      a.append("*")
  
  for i in range(len(a)-x,len(a)):
    for j in range(0,len(a),x):
      b.append(a[i-j])
      
  for p in range(len(b)):
    if("*" in b[p]):
      b[p] = ""
    
  print(''.join(b))