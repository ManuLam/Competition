import math
happyList = []
def isPrime(x):
  for i in range(2,int(math.sqrt(x))+1):
    if(x%i == 0): return False
  return True
  
def happyPrime(x):
  if(x < 10): y,k = str(x**2),0
  else: y,k = str(x),0

  while True:
    for i in range(len(y)):
      k +=  int(y[i])**2
    
    if(k in happyList): return True
    elif(k < 10 and k != 1): return False
    elif(k == 1): 
      happyList.append(x)
      return True
    else: y,k = str(k),0
  
for i in range(int(input())):
  k,x = map(int, input().split())
  if(x == 1 or not isPrime(x)): print("%d %d NO" % (k,x))
  else: print("%d %d YES" % (k,x) if happyPrime(x) and isPrime(x) else "%d %d NO" % (k,x))