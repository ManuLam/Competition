n = int(input())
a = [1] * 5005

for i in range(n+1):
  a[i+1] = (a[i] * (i*2*2 + 2)) // (i + 2)

print(a[n+1])