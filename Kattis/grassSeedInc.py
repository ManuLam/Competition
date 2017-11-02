c,n,cost = float(input()),int(input()),float(0)

for i in range(n):
  a,b = map(float, input().split())
  cost += (a*b)*c
print(cost)