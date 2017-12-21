n = int(input())
a = list(map(int, input().split()))

for i in range(1, len(a)):
  t = a[0]
  for j in range(2,int(a[0])):
    while t % j == 0 and a[i] % j == 0:
      t /= j
      a[i] /= j

  print('%d/%d' % (int(t), int(a[i])))