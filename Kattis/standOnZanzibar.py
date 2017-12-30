for i in range(int(input())):
  k = 0
  a = [int(i) for i in input().split()]
  
  for j in range(len(a)-2):
    if(a[j] < (a[j+1] - a[j])):
        k += (a[j+1] - a[j]*2)
  
  print(k)