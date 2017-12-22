c = 0
while True:
  n,aR = int(input()), []
  c += 1
  if(n == 0): break
  if(c > 1): print()
    
  for i in range(n):
    s = input().split()
    
    for j in range(1,len(s)):
      if(not any(s[j] in sub for sub in aR)):
        aR.append([s[j]])
        
      for x,y in enumerate(aR):
        if(s[j] in y):
          aR[x].append(s[0])
          
  aR = sorted(aR)
  
  for k in range(len(aR)):
    aR[k][1:] = sorted(aR[k][1:])
  
  for k in range(len(aR)):
    print(' '.join(aR[k]))