import collections
s = int(input())
a = [int(x) for x in input().split()]
c = [int(x) for x,y in collections.Counter(a).most_common() if y == 1]

print(a.index(max(c))+1 if len(c) != 0 else "none")