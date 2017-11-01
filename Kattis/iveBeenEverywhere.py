import collections
a = [] 
for i in range(int(input())):
  for j in range(int(input())):
    a.append(input())
  print(len(collections.Counter(a)))
  a.clear()