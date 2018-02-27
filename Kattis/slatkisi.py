a,b = map(int, input().split())
k = a % (10**b)
print((a-k+10**b) if(k >= (10**b)/2) else (a-k)