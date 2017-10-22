mb,n,val = int(input()), int(input()), 0
for x in range(n):
  val += int(input())
print((mb*(n+1))-val)