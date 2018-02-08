a = []
for i in range(int(input())):
  k,s,s1 = 0, input(), ""
  
  for j in range(len(s)):
    s1 += s[j]
    k = max(bin(int(s1)).count("1"), k)
    
  a.append(k)
a = list(map(str,a))

print('\n'.join(a))