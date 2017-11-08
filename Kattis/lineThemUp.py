a = []
b = []
c = []
for i in range(int(input())):
  s = input()
  a.append(s)
  b.append(s)
  c.append(s)
b.sort()
c.sort(reverse = True)

for i in range(len(a)):
  if(a[i] != b[i] and a[i] != c[i]):
    s = "NEITHER"
    break
  elif(a[i] in b[i]):
    s = "INCREASING"

  elif(a[i] in c[i]):
    s = "DECREASING"
    
print(s)