k = {}
while True:
  try:
    s = [x for x in input().split()]
    
    for x,y in enumerate(s):
      if(y.lower() in k): s[x] = k.get(y.lower())
      k[y.lower()] = '.'
    
    print(' '.join(s))
    
  except EOFError:
    break