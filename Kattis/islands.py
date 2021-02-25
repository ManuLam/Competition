m,n = map(int, input().split())

def flood(matrix, row, col, visited):
  if row < 0 or col < 0 or row >= m or col >= n:
    return

  if (matrix[row][col] == 'W') or visited[row][col]:
    return

  visited[row][col] = 1

  flood(matrix, row-1, col, visited)
  flood(matrix, row+1, col, visited)
  flood(matrix, row, col-1, visited)
  flood(matrix, row, col+1, visited)


matrix = [[x for x in input()] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
island_count = 0

for row in range(m):
  for col in range(n):
    if not visited[row][col] and (matrix[row][col] == 'L'):
      flood(matrix, row, col, visited)
      island_count += 1

print(island_count)
