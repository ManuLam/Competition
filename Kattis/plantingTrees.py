n = int(input())
a = sorted(list(map(int, input().split())), reverse = True)

for i in range(n):
  a[i] -= (len(a)-1)-i
  
print(1 + len(a) + max(a))