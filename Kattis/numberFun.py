k = []
for i in range(int(input())):
  a,b,c = map(int, input().split())
  k.append("Possible" if((a + b == c) or (abs(a - b) == c) or (b/a == c) or (a/b == c) or (a*b == c)) else "Impossible")
print('\n'.join(k))