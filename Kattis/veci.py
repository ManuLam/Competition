a,s = [x for x in input()], 0
for i in range(len(a)-1, 0, -1):
  if(a[i-1] < a[i]):
    b = sorted(a[i:])
    for j in range(len(b)):
      if(b[j] > a[i-1]): a[i-1],b[j] = b[j],a[i-1]; break
    s = (''.join(a[:i]) + ''.join(b))
    break
    
print(s)

#brute force solution below
import itertools
y = input()
a = [int(''.join(x)) for x in sorted(set(itertools.permutations([b for b in y]))) if int(''.join(x)) > int(y)]
print(a[0] if len(a) > 0 else 0)
