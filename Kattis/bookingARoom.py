r,n = map(int, input().split())
a = [True] * (r+1)

if(r == n):
  print("too late")

else:
  for i in range(1, n+1):
    a[int(input())] = False
  
  for j in range(1, r+1):
    if(a[j] == True):
      print(j)
      break