a = []
while True:
  m,n = map(int, input().split())
  if(m == 0 and n == 0): break
  drag = [int(input()) for _ in range(m)]
  knight = [int(input()) for _ in range(n)]
    
  if(n < m): a.append("Loowater is doomed!")
  else:
    drag.sort()
    knight.sort()
    i,j,total,k = 0,0,0, True
    
    while(i < m and k):#drag
      while(j < n and knight[j] < drag[i]): j += 1  #knights
      if(j == n): k = False
      
      else: total += knight[j]
      i,j = i+1, j+1
    a.append(total if k else "Loowater is doomed!")
     
print('\n'.join(map(str, a)))