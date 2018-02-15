k,x = [], int(input())
k = [a-1 if a % 10 != 0 else (a - 10**(len(str(a))-len(str(a).rstrip('0')))) for a in [int(input()) for _ in range(x)]]
print('\n'.join(map(str, k)))