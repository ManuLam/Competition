a,b,c = map(int, input().split())
n,m = "=","="
if(a+b == c):
  n = "+"
elif(a-b == c):
  n = "-"
elif(a*b == c):
  n = "*"
elif(a/b == c):
  n = "/"
elif(b+c == a):
  m = "+"
elif(b-c == a):
  m = "-"
elif(b*c == a):
  m = "*"
elif(b/c == a):
  m = "/"
print('%d%s%d%s%d' % (a, n, b, m, c))