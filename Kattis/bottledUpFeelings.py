v,a,b = map(int, input().split())
k,s = v, "Impossible"

if(v % a == 0): s = "%d %d" % (v/a, 0)
else:
  while v > 0:
    v -= b
    if(v % a == 0): 
      s = "%d %d" % (v/a, (k-v)/b)
      break
print(s)