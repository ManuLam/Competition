a = input()
c,k = 0, len(a)

for i in range(int(len(a)/3)):
  s = ""
  for j in range(i,int(len(a)/2)):
    s += a[j]
    c = a.count(s)
    if(c > 1):
      p = len(a)-(c*len(s)) + c + len(s)
      if(p < k): k = p 


print(k)