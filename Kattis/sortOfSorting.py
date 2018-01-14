t = 0
while True:
  n = int(input())
  if(n == 0): break
  a = sorted([input() for i in range(n)], key = lambda x: x[:2])
  print('\n' + '\n'.join(a) if t == 1 else '\n'.join(a))
  t = 1