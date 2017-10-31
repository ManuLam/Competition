n = int(input())

for i in range(n):
  a,b,s = [str(x) for x in input()], [str(x) for x in input()], ""
  for x in range(len(a)):
    s += '.' if(a[x] == b[x]) else '*'
  print(''.join(a))
  print(''.join(b))
  print(s)