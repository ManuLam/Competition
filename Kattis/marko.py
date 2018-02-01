a = [[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
n = int(input())
b,x,k = [input() for x in range(n)], input(), 0

for i in range(len(b)):
  c = 0
  for j in range(len(b[i])):
    if(b[i][j] not in a[int(x[j])-1]):  break
    else: c += 1
  if(c == len(b[i])): k += 1

print(k)