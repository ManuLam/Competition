import collections

def calc(a):
  mul = 1
  for i in range(len(a)): mul *= a[i]+1
  return mul-1

for i in range(int(input())):
  size = int(input())
  s = [input().split()[1] for _ in range(size)]
  print(calc([y for x,y in collections.Counter(s).most_common()]))