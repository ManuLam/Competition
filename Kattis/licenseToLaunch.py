input()
a = list(map(int, input().split()))
b = min(a)

for i in range(len(a)):
  if b == a[i]:
    print(i)
    break