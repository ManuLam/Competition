def check(r,d):
  if((6 < r or r < 0) or (6 < d or d < 0)): return False
  return True

a = [input() for _ in range(7)]
c = 0

for i in range(7):
  for j in range(7):
    if(a[i][j] == '.' and (check(i,j-2) and check(i,j-1)) and (a[i][j-1] == 'o' and a[i][j-2] == 'o')): c += 1
    if(a[i][j] == '.' and (check(i,j+2) and check(i,j+1)) and  (a[i][j+1] == 'o'and a[i][j+2] == 'o')): c += 1
    if(a[i][j] == '.' and (check(i-2,j) and check(i-1,j)) and  (a[i-1][j] == 'o' and a[i-2][j] == 'o')): c += 1
    if(a[i][j] == '.' and (check(i+2,j) and check(i+1,j)) and (a[i+1][j] == 'o' and a[i+2][j] == 'o')): c += 1

print(c)