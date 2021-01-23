N = int(input())

ar = []

for _ in range(N):
  a,b = map(int, input().split())
  ar.append({x for x in range(a, b+1)})

intersection = set.intersection(*ar)

print('gunilla has a point' if intersection else 'edward is right')
