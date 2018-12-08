P,T = map(int, input().split())
c = 0

for i in range(P):
  t = True
  for j in range(T):
    if sum([1 for x in input()[1:] if x.isupper()]) > 0: 
      t = False
  if t:
    c += 1
    
print(c)