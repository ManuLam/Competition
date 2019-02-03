a = [0] * 366

for i in range(int(input())):
  n,m = map(int, input().split())
  for j in range(n,m+1):
    a[j] = 1

print(sum(a))