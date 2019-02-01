def isPrime(x):
  for i in range(2, int(x**.5)+1):
    if x % i == 0: return False
  return True

i,x = 2,1

while x != 10001:
  i += 1
  if isPrime(i): x += 1

print(i)