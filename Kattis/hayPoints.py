m,n = map(int, input().split())
k = {}
for i in range(m):
  s = input().split()
  k[s[0]] = int(s[1])

for i in range(n):
  s = []
  while True:
    t = input()
    if(t == '.'): 
      a = [k.get(y) for y in s if y in k]
      break
    s += t.split()
  
  print(sum(a))