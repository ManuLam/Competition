a,m,n = int(input()), input(), input()
x = sum([1 for i in range(len(m)) if m[i] == n[i]])

print(len(m)-(a-x) if(min(x, a) < a) else a+len(m)-x)