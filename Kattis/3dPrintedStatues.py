n = int(input())

for x in range(1,n+1):
  if(int(2**(x-1)) >= n):
    print(x)
    break