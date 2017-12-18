import collections
d = 0
while True:
  aR,cR,k = [], [], {}
  n = int(input())
  d += 1
  
  if(n == 0):
    break
  
  for i in range(n):
    a = input().split()
    aR.append(a[len(a)-1].lower())
      
  aR.sort()
  
  for x,y in collections.Counter(aR).most_common():
    k[x] = y 
    
  aR = set(aR)
  aR = sorted(list(aR))
  print("List %d:" % d)
  for i in range(len(aR)):
    print("%s | %d" % (aR[i], k.get(aR[i])))