x = [x for x in input()]
a,s = [], 0
for i in range(len(x)-1, 0, -1):
  a.append(x[i])
  if(x[i-1] < x[i]):
    for j in sorted(a):
      if(x[i-1] < j):
        a.append(x[i-1])
        x[i-1] = j
        a.remove(j)
        a.sort()
        s = (''.join(x[:i])+''.join(a))
        break
    break

print(s)