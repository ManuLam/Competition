def method1(n,i):
  if(n % i == 0 or (i*int(n/i+i)*2 == n) or (i*int(n/i+i) + i*int((n+i-1)/i+i) == n)): return True
def method2(n,i):
  if((i*int(n/(i+(i-1))) + (i-1)*int(n/(i+(i-1))) == n) or (i*int((n+i-1)/(i+(i-1))) + (i-1)*(int((n+i-1)/(i+(i-1)))-1) == n)): return True
  
n,a = int(input()), []
print("%d:" % n)

for i in range(2, int(n/2)+2):
  if(method1(n,i)): a.append((i, i))
  if(method2(n,i)): a.append((i,i-1))

a.sort(key = lambda x: x[1])

for item in a:  print("%d,%d" % (item[0],item[1]))