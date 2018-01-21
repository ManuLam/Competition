def merge(a):
  b,c = [],[]
  [b.append(a[i]) if a[i] != 0 else c.append(0) for i in range(4)]
  a = c+b
  
  for i in range(3,0,-1):
    if(a[i] == a[i-1]): a[i],a[i-1] = a[i]*2, 0

  b,c = [],[]
  [b.append(a[i]) if a[i] != 0 else c.append(0) for i in range(4)]
  a = c+b
  
  return a

a = [list(map(int, input().split())) for i in range(4)]
n = input()
b = []

if(n == "0"):
  for i in range(4):  
    print(' '.join(map(str, merge(a[i][::-1])[::-1] )))

elif(n == "2"):
  for i in range(4):  
    print(' '.join(map(str, merge(a[i]))))
    
elif(n == "1"):
  for i in range(4):
    b.append(merge([a[x][i] for x in range(4)][::-1]))

  for i in range(4): 
    print(' '.join(map(str, [b[3-j][3-i] for j in range(4)][::-1])))

elif(n == "3"):
  for i in range(4):
    b.append(merge([a[x][i] for x in range(4)]))
 
  for i in range(4): 
    print(' '.join(map(str, [b[j][i] for j in range(4)])))