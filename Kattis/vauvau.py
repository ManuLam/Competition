a,c,b,d = map(int, input().split())
p,m,g = map(int, input().split())
k = [p,m,g]
dogA = []
dogB = []

for i in range(1, 1000, c+a):
  for j in range(i, i+a):
    dogA.append(j)

for i in range(1, 1000, d+b):
  for j in range(i, i+b):
    dogB.append(j)

for i in range(len(k)):
  if(k[i] in dogA):
    print("both" if k[i] in dogB else "one")
  elif(k[i] in dogB):
    print("one")
  else:
    print("none")