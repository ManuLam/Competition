l,x = map(int, input().split())
c = 0

for i in range(x):
  s = input().split()
  if(s[0] ==  'enter'):
    if(int(s[1]) <= l):
      l -= int(s[1])
    else:
      c += 1
  else:
    l += int(s[1])
    
print(c)