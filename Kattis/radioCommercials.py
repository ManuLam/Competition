x,y = map(int, input().split())
a = list(map(int, input().split()))
mx,k = 0, 0
      
for i in range(x):
  k += a[i] - y
  
  if(mx < k - y): mx = k
  if(k < 0): k = 0

print(mx)