n,m = input().split()
a,b = [x for x in n], [x for x in m]
c = []

for i in range(len(b)):
  if(b[i] in a):
    c.append(b[i])
    a.remove(b[i])
    
print("PASS") if n == ''.join(c) else print("FAIL")