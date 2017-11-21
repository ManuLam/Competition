from collections import defaultdict
k,t = 0,0
p = {}
p = defaultdict(int)

while True:
  try:
    a,b,c = input().split()
    
    if c == 'wrong':
      p[b] += 20
  
    elif  c == 'right':
      k += 1
      t += int(a)
      if(p.get(b) != None):
        t += int(p.get(b))
    
  except ValueError:
    break
  
print(k,t)