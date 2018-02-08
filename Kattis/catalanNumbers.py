x = int(input())
b = [int(input()) for y in range(x)]
m = max(b)
a = [1] * (m+5)

for i in range(m+1):
  a[i+1] = (a[i] * (i*2*2 + 2)) // (i + 2)

print('\n'.join(list(map(str,[a[b[i]] for i in range(x)]))))