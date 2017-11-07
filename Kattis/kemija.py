s = list(input())
v = ['a','e','i','o','u']
for x in range(len(s)-2):
  if s[x] in v:
    s[x+1] = ""
    s[x+2] = ""
print(''.join(s))