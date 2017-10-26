big,index = 0,0
for x in range(5):
  a,b,c,d = map(int, input().split())
  k = (a+b+c+d)
  index = (x+1) if k > big else index
  big = k if k > big else big
print(index, big)
