n = input()
a = list(map(int, input().split()))
a.sort(reverse = True)

b = a[2::3]

print(sum(b))