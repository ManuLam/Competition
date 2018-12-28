n,y = map(int, input().split())
x,a,c = [int(input()) for i in range(y)], [], 0

for i in range(n):
  if(i not in x):
    a.append(i)
  else:
    c += 1

if(n > 0):  print('\n'.join(list(map(str, a))))
print("Mario got %d of the dangerous obstacles." % min(n,c))