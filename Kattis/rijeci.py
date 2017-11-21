a,b = 0,1
for i in range(1,int(input())):
  t = b
  b = a+b
  a = t

print(a,b)