import math
for i in range(int(input())):
  s = input()
  a  = [str(p) for p in s]
  b = []
  x = int(math.sqrt(len(s)))

  for i in range((x-1),-1,-1):
    for j in range(0,len(a),x):
      b.append(a[i+j])
  print(''.join(b))