k,c = [], 0
for i in range(int(input())):
  a = input().split()
  
  if(a[0] not in k): 
    c += 1
    print(a[0], a[1])
    
  k.append(a[0])
  if(c == 12): break