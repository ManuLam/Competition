def check_lines(lines):
  for row in lines:
    half_row_len = len(row)/2
    if row.count('B') != half_row_len or row.count('W') != half_row_len or row.find('BBB') != -1 or row.find('WWW') != -1:
      return 0
  return 1

n = int(input())
rows = [input() for i in range(n)]
columns = [''.join([rows[j][i] for j in range(len(rows[i]))]) for i in range(len(rows))]

print(1 if check_lines(rows) and check_lines(columns) else 0)
