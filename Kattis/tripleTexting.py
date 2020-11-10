from collections import Counter

s = input()
x = int(len(s)/3)

print(Counter([s[0:x], s[x:x*2], s[x*2:]]).most_common()[0][0])
