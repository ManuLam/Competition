n = int(input())

for x in range(n):
  n,m = map(int, input().split())
  s3 = m*(m+1)
  s1 = int(s3/2)
  s2 = s3-m

  print(n,s1,s2,s3)