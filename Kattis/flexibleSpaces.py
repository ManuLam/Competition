w,p = map(int, input().split())
b = list(map(int, input().split()))
b.append(w)
b.insert(0,0)
a = set()

for i in range(len(b)):
  for j in range(i+1,len(b)):
    a.add(abs(b[i]-b[j]))

c = list(a)
c.sort()
print(' '.join(map(str, c)))