import re
for i in range(int(input())):
  a = sorted(set(x for x in "abcdefghijklmnopqrstuvwxyz"))
  b = set()
  s = [x for x in input().lower()]

  for j in range(len(s)):
    if(re.match(r"[a-z]", s[j])):
      b.add(s[j])
  b = sorted(b)

  if(a == b):
    print("pangram")
  else:
    print('missing',''.join(sorted(set(a)-set(b))))