a = []

for i in range(9):
  a.append(int(input()))
  
k = sum(a)-100

for i in a:
  for j in a:
    if(i + j == k and i != j):
      a.remove(i)
      a.remove(j)
      
for i in a:
  print(i)