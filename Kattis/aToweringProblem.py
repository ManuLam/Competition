import random
a = [int(i) for i in input().split()]
c,d = a[-2], a[-1]

while True:
  p,b,k = [], a[:-2], 5
  for i in range(3):
    x = random.randint(0,k)
    p.append(b[x])
    b.remove(b[x])
    k -= 1
  if(sum(p) == c):
    print(' '.join(map(str, sorted(p, reverse = True))), ' '.join(map(str, sorted(b, reverse = True))))
    break
  elif(sum(p) == d):
    print(' '.join(map(str, sorted(b, reverse = True))), ' '.join(map(str, sorted(p, reverse = True))))
    break