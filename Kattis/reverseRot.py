a = [str(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."]
while True:
  try:
    p,q = map(str, input().split())
    b = [str(x) for x in q]
    c = []
    
    for i in range(len(q)):
      k = a.index(b[i])+int(p)
      if(k >= 28):
        k += -28
        
      c.append(a[k])
      
    print(''.join(c)[::-1])
    
  except ValueError:
    break