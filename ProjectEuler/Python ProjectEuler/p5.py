from collections import Counter
primes = [2,3,5,7,11,13,17,19]

def findDiv(n):
  if n == 1:
    return []
  for p in primes:
    if n % p == 0:
      return [p] + findDiv(n / p)

primes_needed = Counter()
for n in range(2, 21):
  pri = Counter(findDiv(n))
  primes_needed = primes_needed | pri
  print(primes_needed)
total = 1
for primes, amount in primes_needed.items():
  total *= primes**amount


print(total)