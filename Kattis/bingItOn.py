x = int(input())
k,a = {}, [0] * x

for i in range(x):
  newk = k

  for j in input():
    if(j not in newk):
      newk[j] = {'': -1}
      
    newk = newk[j]
    newk[''] +=  1

  a[i] = newk['']
  
  
print('\n'.join(list(map(str,a))))