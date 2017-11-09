r,c = map(int, input().split())
aR,aC,a,b,p = [],[],[],[],[]

for i in range(r):
  s = input()
  aR.append(s)
  
x = 1  
for i in range(c):
  s = ""
  for j in range(r):
    s += aR[j][x-1:x]
    
  aC.append(s)
  x += 1

for i in aR:
  a.append(i)

for i in aC:
  a.append(i)
  
for i in a:
  p = list(map(str, i.split('#')))
  for j in p:
    if(len(j) > 1):
      b.append(j)

a.sort()
b.sort()
print(b[0])