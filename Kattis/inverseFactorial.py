import math
n = input()
m = len(n)
a,i = 0, 1
k = {'1': 1, '2': 2, '6': 3, '24': 4, '120': 5}

if(n in k): 
  print(k[n])
else:
  while True:
    a += math.log10(i)
    if(a > m): 
      print(i-1)
      break
    i += 1