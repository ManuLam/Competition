N = int(input())
pieces = list(map(int, input().split()))
t = 1

for i in range(N-1):
    if pieces[i+1] > pieces[i]:
        t += 1

print(t)
