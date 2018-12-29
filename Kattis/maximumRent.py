a,b = map(int, input().split())
m,o = map(int, input().split())

print(a*(m-1) + b*(1) if a > b else a*max(1, o-m) + b*(m-max(1, o-m)))