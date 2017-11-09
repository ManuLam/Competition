n,t = map(int, input().split())
a,b = list(map(int, input().split())), 0

for x in a:
  t -= x
  if(t < 0):
    break;
  b += 1
  
print(b)