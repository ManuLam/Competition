x,y = [],[]
s1,s2 = input().split()

for i in range(len(s1)):
  for j in range(len(s2)):
    if s1[i] == s2[j]:
      x.append(j)
      y.append(i)

a = [['.' for i in range(len(s1))] for j in range(len(s2))]
  
for down in range(len(s2)):
  for across in range(len(s1)):
    if across == y[0]:  print(s2[down], end="")
    elif down == x[0]:  print(s1[across], end="")
    else: print(".", end="")

  print()