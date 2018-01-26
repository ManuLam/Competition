b,k,g = map(int, input().split())
x = int(k/g)

print(int((b-1) / x) if((b-1) % x == 0) else int((b - 1) / x + 1 ))