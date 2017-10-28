l,d,x = input(),input(),input()
n,m,c = 0,0,0
for j in range(int(l),int(d)+1):
  a = [int(i) for i in str(j)]
  if(sum(a) == int(x)):
    c += 1
    n = ''.join(str(x) for x in a) if c == 1 else n
    m = ''.join(str(x) for x in a)
print(n + "\n" + m)