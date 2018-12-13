def digitSum(x):
   total = 0
   while x:
       total, x = total+(x%10), x//10
   return total

def carryCount(a, b):
    return (digitSum(a) + digitSum(b) - digitSum(a+b))/9

while(True):
  n,m = map(int, input().split())
  if(n == 0 and m == 0): break
  c = carryCount(n,m)

  if c > 0:
    print("%d carry operations." % (c) if c > 1 else "1 carry operation.")
  else:
    print("No carry operation.")