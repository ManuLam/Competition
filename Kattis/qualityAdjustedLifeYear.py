x = 0
for i in range(int(input())):
  n,m = map(float, input().split())
  x += m*n

print("{0:.3f}".format(x))