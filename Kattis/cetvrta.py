import collections
a,b = [],[]
for i in range(3):
  c,d = map(int, input().split())
  a.append(c)
  b.append(d)

aT = [int(x) for y,x in enumerate(collections.Counter(a).most_common()[-1])]
bT = [int(x) for y,x in enumerate(collections.Counter(b).most_common()[-1])]

print(aT[0],bT[0])