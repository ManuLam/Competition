r = []
n = []

for i in range(int(input())):
  a,b = input().split()
  
  if(a.isdigit()):
   r.append(int(a))
   n.append(b)
    
  else:
    r.append(int(b)*2)
    n.append(a)
    
for i in range(len(r)):
  for j in range(i+1,len(r)):
    if(r[i] > r[j]):
      r[i], r[j] = r[j], r[i]
      n[i], n[j] = n[j], n[i]

print('\n'.join(n))