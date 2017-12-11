c = 0
for i in range(10):
  try:
    e,m = map(int, (input().split()))
    c += 1
    t = 0
    
    if(e != 0):
      t = 365 - e
      m = (m+t)%687
      e = 0
      
    while(m != 0):
      m = (m+365)%687
      t += 365
      
    print("Case %d:" % c, t)
      
  except EOFError:
    break