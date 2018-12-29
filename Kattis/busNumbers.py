a,find,t = [1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464, 171288, 195841, 216027, 216125, 262656, 314496, 320264, 327763, 373464], int(input()), False

for i in range(len(a)-1,-1,-1):
  if a[i] <= find:
    t = True
    break
print(a[i] if t else 'none')

'''
import collections
a,b = [i**3 for i in range(1,int(400000**(1/3)))], []
for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i]+a[j] <= 400000:
      b.append(a[i]+a[j])

c,t = sorted([x[0] for x in collections.Counter(b).most_common() if x[1] > 1]), False

for i in range(int(input()), 1728, -1):
  if i in c:
    t = True
    break
print(c)
print(i if t else 'none')'''