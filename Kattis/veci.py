a,s = [x for x in input()], 0
for i in range(len(a)-1, 0, -1):
  if(a[i-1] < a[i]):
    b = sorted(a[i:])
    for j in range(len(b)):
      if(b[j] > a[i-1]): a[i-1],b[j] = b[j],a[i-1]; break
    s = (''.join(a[:i]) + ''.join(b))
    break
    
print(s)
