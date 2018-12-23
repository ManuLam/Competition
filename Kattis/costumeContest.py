import collections
size = int(input())
a = [input() for _ in range(size)]
c = collections.Counter(a).most_common()

print('\n'.join(sorted([x for x,y in c if y == c[-1][1]], key = str.lower)))