import collections
n1, c = int(input()), 0

for i in range(n1):
  n2 = int(input())
  a = [str(x) for x in input().split()]
  least_common = collections.Counter(a).most_common()[-1]
  c += 1
  print("Case #%d:" % c, least_common[0])