import collections
s = list(input())

k,c = 0,0
a = collections.Counter(s).most_common()
for x,y in a:
  if(y%2 != 0):
    k += 1
    c += 1
    if(c == 1):
      k = 0

print(k)