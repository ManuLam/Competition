n = int(input())
x,c = 2, 1

while(x**2 <= n):
  if(n%x == 0):
    n /= x
    c += 1
  else: x += 1

print(c)