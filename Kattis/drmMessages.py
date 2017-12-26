s = input()
k = int(len(s)/2)
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

c = [alpha.index(i) for i in s[:k]]
cS = sum(c)%26
s1 = [alpha[(alpha.index(i)+cS)%26] for i in s[:k]]

d = [alpha.index(i) for i in s[k:]]
dS = sum(d)%26
s2 = [alpha[(alpha.index(i)+dS)%26] for i in s[k:]]

o = 0
for i in s1:
  s1[o] = alpha[(alpha.index(i) + alpha.index(s2[o]))%26]
  o += 1

print(''.join(s1))