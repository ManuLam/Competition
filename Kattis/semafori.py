n,l = map(int, input().split())
t,td = 0, 0

for i in range(n):
  d,r,g = map(int, input().split())
  
  t += d - td
  td = d
  
  if((t % (r+g)) < r):
    t += r - (t % (r+g))

print(t + (l - td))