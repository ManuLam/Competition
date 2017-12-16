a,b = 0,0

for i in range(int(input())):
  c,d = map(int, input().split())
  a += c*60
  b += d
  
print(round(b/a, 7) if b > a else "measurement error")