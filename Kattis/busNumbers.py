n = int(input())
a = sorted([int(x) for x in input().split()])
c = 1

for i in range(1, n+1):
  
  if(i < n and a[i-1] == a[i]-1 ):
    c += 1
  
  else:
    if(c >= 3):
      print('%d-%d' % (a[i-c], a[i-1]) , end = " " if i < n else "\n")
      
    else:
      while(c >= 1):
        print('%d' % (a[i-c]) , end = " " if i < n else "\n")
        c -= 1  
    c = 1