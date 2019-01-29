x = 600851475143 
rt = int(x**.5)

def isPrime(x):
  for i in range(2, int(x**.5)+1):
    if x % i == 0: return False
  return True

for i in range(rt, 2, -1):
  if isPrime(i) and x % i == 0:
    print(i)
    break