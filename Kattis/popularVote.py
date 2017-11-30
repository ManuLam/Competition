for i in range(int(input())):
  a,b = [],[]
  for j in range(int(input())):
    a.append(int(input()))
  
  k,m = max(a), a.index(max(a))
  b = [int(i) for i,j in enumerate(a) if j == k]
  
  if(len(b) > 1):
    print("no winner")
    
  elif(a[b[0]] > abs(sum(a)-a[b[0]])):
    print("majority winner %d" % (m+1))
    
  elif(a[b[0]] <= abs(sum(a)-a[b[0]])):
    print("minority winner %d" % (m+1))