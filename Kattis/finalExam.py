n = int(input())
ar = [input() for _ in range(n)]


cur = ar[0]
same = 0
ans = 0

for i in range(1, n):
    if cur == ar[i]:
        same += 1
    
    else:
        ans += max(0, same)
        cur = ar[i]
        same = 0
    
ans += max(0, same)    
print(ans)
