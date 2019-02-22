grid,path = 20,1

for i in range(grid):
  path *= (2*grid) - i
  path //= i + 1

print(path)