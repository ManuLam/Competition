a = [['A','B','C'], ['B','A','B','C'] ,['C','C','A','A','B','B']]
n,s,c,k = int(input()), [x for x in input()], [0, 0, 0], ['Adrian', 'Bruno', 'Goran']

for i in range(len(s)):
  for j in range(len(a)):
    if(s[i] == a[j][i % len(a[j])]):
      c[j] += 1
    
m = max(c[0],c[1],c[2])
print(m)
for i in range(len(c)):
  if(c[i] == m):
    print(k[i])