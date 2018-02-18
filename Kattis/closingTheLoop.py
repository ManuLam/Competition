c = []
for i in range(int(input())):
  a,b = [],[]
  j,t = input(), input().split()
  
  for j in range(len(t)):
    if(t[j][-1] == 'R'):
      a.append(int(t[j][:-1]))
    elif(t[j][-1] == 'B'):
      b.append(int(t[j][:-1]))
      
  n = min(len(a),len(b))
  a.sort(reverse = True)
  b.sort(reverse = True)
  p,k = 0,-n*2
  
  while(p < n):
    k += (a[p] + b[p]) 
    p += 1
  
  c.append('Case #%d: %d' % (i+1, k))
print('\n'.join(c))