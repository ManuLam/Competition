alpha = "abcdefghijklmnopqrstuvwxyz"
n,m = map(int, input().split())
s1,s2 = input(),input()
a = ['']  *(n+m)

for i in range(n):
  a[m + i] = s1[i]

for i in range(m-1,n-1,-1):
  a[i] = alpha[(-ord(a[i + n]) + ord(s2[i]) + 26) % 26]
  
print(''.join(a))