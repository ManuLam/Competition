for i in range(int(input())):
  a = [int(x) for x in input().split()]
  start = a[0]
  a = a[1:]
  d = a[1] - a[0]
  
  for j in range(1, len(a)):
    if(a[j] - a[j-1] == d and j == len(a)-1):
      print("arithmetic")
      break
    
    elif(a[j] - a[j-1] != d):
      a.sort()
      d = a[1] - a[0]
      
      for k in range(1, len(a)):
        if(a[k] - a[k-1] == d and k == len(a)-1):
          print("permuted arithmetic")
          break
        
        elif(a[k] - a[k-1] != d):
          print("non-arithmetic")
          break
        
      break