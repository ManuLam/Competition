a = [1,2,3]
s = [str(x) for x in input()]

for x in range(len(s)):
  if(s[x] == 'A'):
    a[0],a[1] = a[1],a[0]
    
  elif(s[x] == 'B'):
    a[1],a[2] = a[2],a[1]
    
  elif(s[x] == 'C'):
    a[0],a[2] = a[2],a[0]

print(a.index(1)+1)