a,pr = [], 1
for i in range(int(input())):
  p,q = input().split()
  a.append(float(q))

a.sort()
for i in range(len(a)):
  pr += sum(a[:i])

print(round(pr, 4))