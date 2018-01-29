import collections
print(sum(y for x,y in collections.Counter([x for x in input()]).most_common()[::-1][:-2]))