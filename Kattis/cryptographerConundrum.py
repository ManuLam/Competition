s,i,j,h = [str(x) for x in input()], 0, 0, ['P','E','R']

for x in range(len(s)):
  if(j == 3):
    j = 0
  if(s[x] != h[j]):
    i += 1
  j += 1
print(i)