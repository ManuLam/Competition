for  i in range(int(input())):
  diy,m = map(int,input().split())
  d = list(map(int,input().split()))
  c,k = 0,0
  
  for j in range(m):
    if((d[j] >= 13) and ((k+12) % 7 == 5)): c += 1
    k = (k+d[j]) % 7

  print(c)